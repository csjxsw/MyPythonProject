#!/usr/bin/env python
# coding=utf-8

db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another,please: '
            continue
        else:
            pwd = raw_input("input your password,please: ")
            db[name] = pwd
            break


def olduser():
    name = raw_input("login: ")
    pwd = raw_input("password: ")
    password = db.get(name)
    if password == pwd:
        print 'welcome back ', name
    else:
        print 'login incorrect'


def showmenu():
    prompt = """
    (N)ew User login
    (E)xisting User loing
    (Q)uit

    Enter choice:"""

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'invalid option , try again'
            else:
                chosen = True
                done = True
    if choice == 'n':
        newuser()
    elif choice == 'e':
        olduser()
    elif choice == 'q':
        exit()
    showmenu()


showmenu()