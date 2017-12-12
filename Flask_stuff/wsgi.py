#!/usr/bin/env python3

from runtime import forest

if __name__ == "__main__":
    # if this is in production:
    #   - Don't forget to change host to 0.0.0.0
    #   - Don't for get to change debug to False
    forest.run(host = '127.0.0.1', port = 5000, debug = True)