from flask import render_template, Flask, request, make_response, send_from_directory
import os

def get_filelist():
    filelist = os.listdir("upload/")
    return filelist

app = Flask(__name__)

@app.route('/')
def hello(filelist=[]):
    return render_template("index.html", filelist=get_filelist())

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(f"upload/{f.filename}")
        filelist = get_filelist()
        return render_template("index.html", filelist=filelist)
    else:
        return render_template("index.html", filelist=get_filelist())

@app.route('/download/<filename>',methods=['GET'])
def download(filename):
    response = make_response(send_from_directory("upload", filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)