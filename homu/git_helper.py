#!/usr/bin/env python3

import sys
import os

def main():
    args = ['ssh', '-i', os.getenv('HOMU_GIT_KEY_PATH'), '-S', 'none'] + sys.argv[1:]
    os.execvp('ssh', args)

if __name__ == '__main__':
    main()
