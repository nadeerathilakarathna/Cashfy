//alert('script.js is connected');
var htmldata = '';
var default_selection = false;
var account_dropdown = '';

var chart = '';



function focusLogin() {
  var inputElement = document.getElementById("email");
  inputElement.focus();
  document.getElementById("login").scrollIntoView({ behavior: 'smooth' });
}

function focusSignUp() {
  var inputElement = document.getElementById("firstname");
  inputElement.focus();
  document.getElementById("login").scrollIntoView({ behavior: 'smooth' });
}



function removeAllContents(className) {
  const container = document.querySelector(`.${className}`);
  if (container) {
    container.innerHTML = ''; // Set innerHTML to an empty string
  } else {
    console.error(`Element with class '${className}' not found.`);
  }
}

function hello() {
  alert("Hello world");
}




function createicons() {
  htmldata = '';
  for (var icon of iconNames) {
    var query = `
    <input type="radio" name="icon" value="${icon}" id="${icon}" required/>
    <label for="${icon}">
      <span class="material-symbols-outlined">${icon}</span>
    </label>
    `;
    htmldata = htmldata + query;
  }
}






function addAccount() {
  htmldata = '';
  createicons();
  const popupsContainer = document.querySelector('.popups');

  const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
  var formHTML = `
  <div class="popup-box">
    <button class="close" onclick="removeAllContents('popups');">&times;</button>

  <form action="createaccount" method="post" id='createaccount'>

  <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}" id="csrf">

    <label for="" class="title">Add Account</label>
    <div class="content">
      <input type="text" name="account" id="account" placeholder="Account Name" class="name" required>
      <br>
      <input type="number" name="initial" id="initial" placeholder="Initial balance" class="initial" required>
      <br>
      <div class="container-box">
        ${htmldata}
      </div>
    </div>
    <button type="submit" class="submit" onclick="console.log('hello');">Add</button>
  </form>
  </div>
`;
  popupsContainer.innerHTML = formHTML;
}









function addExpense() {
  htmldata = '';
  createicons();
  const popupsContainer = document.querySelector('.popups');

  const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
  var formHTML = `
  <div class="popup-box">
    <button class="close" onclick="removeAllContents('popups');">&times;</button>

  <form action="createexpense" method="post" id='createexpense'>

  <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}" id="csrf">

    <label for="" class="title">Add Expense Category</label>
    <div class="content">
      <input type="text" name="expanse" id="expense" placeholder="Category Name" class="expense" required>
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


function addIncome() {
  htmldata = '';
  createicons();
  const popupsContainer = document.querySelector('.popups');

  const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
  var formHTML = `
  <div class="popup-box">
    <button class="close" onclick="removeAllContents('popups');">&times;</button>

  <form action="createincome" method="post" id='createincome'>

  <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}" id="csrf">

    <label for="" class="title">Add Income Category</label>
    <div class="content">
      <input type="text" name="income" id="income" placeholder="Category Name" class="income" required>
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



function openPopupTransaction(id, name, icon) {
  const popupsContainer = document.querySelector('.popups');
  const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

  const currentDate = new Date();
  const formattedDate = currentDate.toISOString().split('T')[0];

  var formHTML = `
    <div class="popup-box" id="popup_categories">
        <button class="close" onclick="removeAllContents('popups');">&times;</button>

        <form action="createtransaction" method="post" id='createtransaction'>

            

            <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}" id="csrf">
            <input type="hidden" name="category_id" value="${id}" id="category_id">
            
            <span class="material-symbols-outlined img" id="category_image">${icon}</span>
            <br>
            <label for="" class="category" id="category_name">${name}</label>

            <div class="content">
                <input type="date" name="date" id="date" value="${formattedDate}" max="${formattedDate}" required>
                <br>

                <select id="dropdown" name="dropdown">
                    <option value="option1">Option 1</option>
                    <option value="option2" selected>Option 2</option>
                    <option value="option3">Option 3</option>
                    
                </select>

                <br>
                <input type="number" name="amount" id="amount" placeholder="Amount " class="amount" required>
                <br>
                <input type="text" name="description" id="description" placeholder="Description" class="description">

                <br>
            </div>
            <button type="submit" class="submit" onclick="console.log('hello');">Add</button>
        </form>
    </div>
  `;

  popupsContainer.innerHTML = formHTML;
  var dropdown_menu = $("#dropdown");
  dropdown_menu.empty();
  dropdown_menu.append(account_dropdown)
}

