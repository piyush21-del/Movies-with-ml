{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e984b66e-9e62-4f1f-ba66-eb0e7c181c50",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'movies.pkl'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpickle\u001b[39;00m\n\u001b[32m      4\u001b[39m \u001b[38;5;66;03m# load data\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m movies = pickle.load(\u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mmovies.pkl\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mrb\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m)\u001b[49m)\n\u001b[32m      6\u001b[39m similarity = pickle.load(\u001b[38;5;28mopen\u001b[39m(\u001b[33m'\u001b[39m\u001b[33msimilarity.pkl\u001b[39m\u001b[33m'\u001b[39m,\u001b[33m'\u001b[39m\u001b[33mrb\u001b[39m\u001b[33m'\u001b[39m))\n\u001b[32m      8\u001b[39m \u001b[38;5;66;03m# recommendation function\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:343\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    336\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    337\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    338\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    339\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    340\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    341\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m343\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'movies.pkl'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "\n",
    "# load data\n",
    "movies = pickle.load(open('movies.pkl','rb'))\n",
    "similarity = pickle.load(open('similarity.pkl','rb'))\n",
    "\n",
    "# recommendation function\n",
    "def recommend(movie):\n",
    "    movie_index = movies[movies['title'] == movie].index[0]\n",
    "    distances = similarity[movie_index]\n",
    "    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]\n",
    "\n",
    "    recommended_movies = []\n",
    "    for i in movies_list:\n",
    "        recommended_movies.append(movies.iloc[i[0]].title)\n",
    "    return recommended_movies\n",
    "\n",
    "# UI\n",
    "st.title('🎬 Movie Recommender System')\n",
    "\n",
    "selected_movie = st.selectbox(\n",
    "    \"Select a movie\",\n",
    "    movies['title'].values\n",
    ")\n",
    "\n",
    "if st.button('Recommend'):\n",
    "    recommendations = recommend(selected_movie)\n",
    "    for movie in recommendations:\n",
    "        st.write(movie)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce61d2d1-8082-4b53-9cf1-31b29ffca8bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "streamlit run app.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
