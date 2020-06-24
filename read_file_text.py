from flask import Flask, render_template, request
import codecs

app = Flask(__name__)


@app.route('/read_file_text/', methods=['GET'])
def read_file_text():
    try:
        file = request.args.get('file', 'file1') #Get file name from query parameters
        start = int(request.args.get('start', 0)) #Get Start line number from query parameters
        end = int(request.args.get('end', -1)) #Get End line number from query parameters
        file_name = 'text_files\\file_name.txt'.replace('file_name', file) #set file path
        encodings = ['utf-8', 'utf-16'] #encodings list
        for e in encodings:
            try:
                f = codecs.open(file_name, 'r', encoding=e)
                file_data = f.readlines()
                if(end == -1): 
                    end = len(file_data) #get end line number i.e. length from file
                file_data = ''.join(file_data[start:end+1]) #convert list to string
            except UnicodeDecodeError as ude:
                exception_detail = ude 
            else:
                exception_detail = 'No Exception' 
                break    
        if exception_detail == 'No Exception': #if there is no exception
            return render_template('filedata.html', output_data=file_data)
        else: #if there is UnicodeDecodeError exception
            return render_template('filedata.html', output_data=exception_detail)
    except Exception as ex: #if any other exception 
        exception_detail = ex
        return render_template('filedata.html', output_data=exception_detail)


if __name__ == "__main__":
    app.run(debug=True)
