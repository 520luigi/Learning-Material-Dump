#!/usr/bin/python
import sys

def capitalize(s):
  return ' '.join(w[:1].upper() + w[1:] for w in s.split(' '))

def main():
    if (len(sys.argv) == 2):
        print(capitalize(sys.argv[1]))

if __name__ == '__main__':
    main()
