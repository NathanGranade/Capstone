import React from 'react';
  
function Register () {
    return     <div class="login-form">
    <h1>Sign up for clab</h1>
<form action="/login" method = "POST">
    <p>Email <input id="email" type = "text" name = "email" placeholder="email"/></p>
    <p>Username <input id="username" type = "text" name = "username" placeholder="username"/></p>
    <p>Password <input id="password" type = "password" name = "password" placeholder="password"/></p>
<p><input class="button-19" id="submit" type = "submit" value = "Register" /></p>
</form>
<div class="controls">
<p id="response"></p>
</div>
</div>

}
export default Register;