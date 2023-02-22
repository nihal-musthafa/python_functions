<h2 class="bg-primary">profile</h1>
    <div class="row">
   <div class="col">
    <div class="card" style="width: 18rem;">
        <img class="card-img-top" src="{{request.user.p_user.profile_pic.url}}" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">{{request.user.first_name}} {{request.user.last_name}}</h5>
          <p class="card-text">i am {{request.user.p_user.age}} years old</p>
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item"> gender:{{request.user.p_user.gender}}</li>
          <li class="list-group-item"> email: {{request.user.p_user.email}}</li>
          <li class="list-group-item">phone: {{request.user.p_user.phone}}</li>
        </ul>
        <div class="card-body">
          <a href="#" class="card-link">Card link</a>
          <a href="#" class="card-link">Another link</a>
        </div>
      </div>

   </div>
   
   <div class="col-4" style="border-left:2px solid black;height: 650px;">
    <a href="{% url 'addpro' %}" class="btn btn-warning">Add Profile</a>
</div>
   </div>
{% endblock nav %}
