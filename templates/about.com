{% extends "layout.html" %}
  
{% block content %}
  <h2>About</h2>
  <p>This is an About page for the Intro to Flask article. Don't I look good? Oh stop, you're making me blush.</p>
{% endblock %}