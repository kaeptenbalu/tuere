#/usr/bin/python2

from flask import Flask, render_template, request, url_for
import subprocess
from datetime import datetime
import time
from threading import Thread


'----------------------> Helpers <-----------------------------'
def write_file(path, value):
    try:
        with open(path,'w') as file:
            file.write(value)
    except: 
	print "Fehler"
	pass

        #Maschine starten


'-----------------------> Initialisierung <--------------------'
write_file('/sys/class/gpio/export','22')
write_file('/sys/class/gpio/gpio22/direction','out')


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def do():

    go = request.args.get('go')

    if go is not None:	
	write_file('/sys/class/gpio/gpio22/value','0')	
	time.sleep(5)
        write_file('/sys/class/gpio/gpio22/value','1')



    return render_template('form.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)






