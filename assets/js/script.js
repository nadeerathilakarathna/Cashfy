//alert('script.js is connected');
var htmldata ='';

function focusLogin() {
    var inputElement = document.getElementById("email");
    inputElement.focus();
  }

function focusSignUp(){
    var inputElement = document.getElementById("firstname");
    inputElement.focus();
}



function removeAllContents(className) {
  const container = document.querySelector(`.${className}`);
  if (container) {
    container.innerHTML = ''; // Set innerHTML to an empty string
  } else {
    console.error(`Element with class '${className}' not found.`);
  }
}

function hello(){
  alert("Hello world");
}




function createicons(){
  
  for (var icon of iconNames) {
    var query = `
    <input type="radio" name="account" id="${icon}" required/>
    <label for="${icon}">
      <span class="material-symbols-outlined">${icon}</span>
    </label>
    `;
    htmldata = htmldata + query;
  }
}



function addAccount(){
  const popupsContainer = document.querySelector('.popups');

  var formHTML = `
  <div class="popup-box">
    <button class="close" onclick="removeAllContents('popups');">&times;</button>

  <form action="createacc" method="post">
    <label for="" class="title">Add Account</label>
    <div class="content">
      <input type="text" name="account" id="account" placeholder="Account Name" class="name">
      <br>
      <input type="number" name="initial" id="initial" placeholder="Initial balance" class="initial">
      <br>
      <div class="container-box">
        ${htmldata}
      </div>
    </div>
    <button type="submit" class="submit">Add</button>
  </form>
  </div>
`;
popupsContainer.innerHTML = formHTML;
}