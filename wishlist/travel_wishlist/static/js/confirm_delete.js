// Find all the delete buttons, add a click event listener to all buttons
// On click event, show a confirm dialog
// Browsers will handle these events before the click that submits the form
// to provide the opportunity to intercept the form submit with JavaScript.
// If the click event handler prevents the event propagating, the form submit
// never happens.  If the click event doesn't prevent the event propagating,
// the form will be submitted as usual.

var deleteButtons = document.querySelectorAll('.delete');

deleteButtons.forEach(function(button){

  button.addEventListener('click', function(ev){

    // Show a confirm dialog
    var okToDelete = confirm("Delete place - are you sure?");

    // If user presses no, prevent the browser from submitting the form to the server
    if (!okToDelete) {
      ev.preventDefault();  // Prevent the click event propagating
    }

    // Otherwise, the web page will continue processing the event, 
    // and send the delete request to the server.

    //Javascript is static files. They are the same no matter the user, and they don't change. Style sheets, and Image files are also static. Dynamic files are created through app code, they could be
    //different between users. Static & dynamic files are hosted seperately? 
  })
});