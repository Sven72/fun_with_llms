{% block content %}
 {% for emotion in emotions %}
    <div class='emo'>
        <h2>{{ emotion['label'] }}</h2>
        <p>{{ emotion['example'] }}</p>
        <p>{{ emotion['explanation'] }}</p>
        <p>{{ emotion['etymology'] }}</p>
        <p>{{ emotion['created'] }}</p>
    </div>
    {% endfor %}
{% endblock %}