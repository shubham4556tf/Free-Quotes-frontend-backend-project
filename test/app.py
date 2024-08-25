from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

quotes = {
    "Albert Einstein": ["Imagination is more important than knowledge."],
    "Mahatma Gandhi": ["Be the change that you wish to see in the world."],
    "Nelson Mandela":[ "It always seems impossible until it’s done."]
}
#Qutoes For peronal author
   #here key requee to match from url key
author_quotes = {   # To access this use for loop in js
    "alberteinstein":["Imagination is more important than knowledge.",'static.image.jpg']   ,
    "MahatmaGandhi":[],
    "Nelson Mandela":[]
}

#Image of pernality
# Quotes dict return in webpage.
@app.route("/", methods=['GET'])
def index():
 
  
    return render_template('index.html', quotes=quotes)  # dict can access and using loop in dict u can access key and value
@app.route("/", methods=['POST'])
def count():
    i = range(1,101)
    return render_template('index.html',i=i)
  

# For Personal Author Quotes.



# This will give the search result
@app.route("/data", methods=['GET'])
def search_quotes():
    query = request.args.get("query_html")   # query var is responsible for input of search box
    if query:
        quote = quotes.get(query)   # quote = dict value
        if quote:
            return jsonify({query.replace(" ",""): quote[0]})  # This will give me jsonify: query ==> key and quote ==> value
        else:
            return jsonify({"error": "Quote not found!"})  # Return JSON object when quote isn't found
    return jsonify({"error": "No query parameter provided"}), 400  # Return JSON object when no query is provided

# This will give the search result
@app.route("/author/<id>", methods=['GET'])
def authorPage(id):
    qt = author_quotes.get(id)
    return render_template('author.html',qt=qt,id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



    
''' logic of serch apage


= > use div and use <quotes dict> 
 then access image and quotes from that.
 for seach use same.
'''