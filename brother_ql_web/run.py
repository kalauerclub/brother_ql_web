#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app

def main():
    app = create_app()
    app.run(host = app.config['SERVER_HOST'], port = app.config['SERVER_PORT'])

if __name__ == "__main__":
    main()
