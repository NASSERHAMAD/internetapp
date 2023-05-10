var form = document.querySelector("#contact-form");

form.addEventListener("submit", function(event) {
event.preventDefault();

var nameInput = document.querySelector("#name");
var emailInput = document.querySelector("#email");
var messageInput = document.querySelector("#message");

var name = nameInput.value.trim();
var email = emailInput.value.trim();
var message = messageInput.value.trim();

if (name === "" || email === "" || message === "") {
alert("Please fill in all fields");
} else {
alert("Thank you for contacting us, " + name + "! We will respond to your message at " + email + " as soon as possible.");
form.reset();
}
});