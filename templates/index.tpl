

<iframe
  src="{{ gradioserver_url }}"
  width="100%"
  height="400"
  frameborder="0"
></iframe>
<h2>This is what others feel. And maybe you</h2>
 {% for emotion in emotions %}
    <div class='emo'>
        <h2>{{ emotion['label'] }}</h2>
        <p>{{ emotion['example'] }}</p>
        <p>{{ emotion['explanation'] }}</p>
        <p>{{ emotion['etymology'] }}</p>
    </div>
{% endfor %}