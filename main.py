from youtube_comment_scraper_python import youtube
import streamlit as st

def Youtube_Comment_Extractor(URL):
    youtube.open(URL)
    for i in range(0, 2):
        res = youtube.video_comments()
        data = res['body']
        comments = data
    comments_values = []
    l = len(comments)
    only_comments = []
    for i in range(l):
        comments_values.append(comments[i])
        only_comments.append(comments_values[i].values())
    #labels
    COMMENTS = []
    LIKES = []
    TIMELINE = []
    
    for i in only_comments:
        COMMENTS.append(list(i)[0])
        LIKES.append(list(i)[1])
        TIMELINE.append(list(i)[2])
    data = {'Comments': COMMENTS,
            'Likes': LIKES,
            'Timeline': TIMELINE}
    return data, TIMELINE
    


st.title('Youtube **:blue[Comment]** Extractor')
st.subheader('Powered by **:red[Stream]**')
st.subheader('Made by **:green[S.D.B]**')
input = st.text_input('Enter the YouTube URL')
if st.button('Submit'):
    st.success('Your output is here')

    D,timeline = Youtube_Comment_Extractor(input)
    st.table(D)
    st.title('Analysis')
    st.subheader('Line chart')
    st.line_chart(D)
    