from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import pandas
import numpy as np

app=Flask(__name__)
popular_df=pickle.load(open('popular.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similar_df=pickle.load(open('similarity_scores.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))


@app.route('/')
def index():
    return render_template("index.html",
                           authors=list(popular_df['Book-Author'].values),
                           book_names=list(popular_df['Book-Title'].values),
                           images=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['rating_count'].values),
                        avg_rating=list(popular_df['average_rating'].values))
@app.route('/recommend')
def recommend_ui():
    return render_template("recommend.html")

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input=request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similar_df[index])), key=lambda x: x[1], reverse=True)[1:9]  # top5
    data = []
    for i in similar_items:
        items = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(items)
        print(data)

    return render_template("recommend.html",data=data)


    return "hello world"
if __name__=='__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
