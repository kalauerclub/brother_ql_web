{
  description = "Application packaged using poetry2nix";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  inputs.poetry2nix = {
    url = "github:nix-community/poetry2nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication overrides;
        pkgs = nixpkgs.legacyPackages.${system};
        inv_pkg = self.packages."${system}".brother_ql_web;
      in
      {
        packages = {
          brother_ql_web-docker = pkgs.dockerTools.buildImage {
            name = "brother_ql_web-docker";
            config = {
              Cmd = [ "${inv_pkg}/bin/brother_ql_web" ];
            };
          };
          brother_ql_web = mkPoetryApplication {
            projectDir = self;
            propagatedBuildInputs = [ pkgs.fontconfig ];
            overrides = overrides.withDefaults
              (self: super: {
                pillow = super.pillow.override {
                  preferWheel = true;
                };
               flask-bootstrap4 = super.flask-bootstrap4.overridePythonAttrs
                (
                  old: {
                    buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                  }
                );
              });
          };
          default = inv_pkg;
        };

        devShells.default = pkgs.mkShell {
          packages = [ poetry2nix.packages.${system}.poetry ];
        };
      });
}
