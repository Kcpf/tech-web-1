// Get the modal
var modal = document.getElementById("modal");

// Get the buttons that opens the modal
var btns = document.getElementsByClassName("card-edit-button");

// Get the <span> elements that closes the modal
var spans = document.getElementsByClassName("close");

var noteId = "";
var modalTitle = document.getElementById("modal-title-text");
var modalContent = document.getElementById("modal-content-text");
var modalTag = document.getElementById("modal-tag-text");
var modalUpdateButton = document.getElementById("modal-update-button");

// When the user clicks on the button, open the modal
for (let btn of btns) {
  btn.onclick = () => {
    let [title, content, tag, id] = btn.value.split("&");

    modal.style.display = "block";
    modalTitle.innerHTML = title;
    modalContent.innerHTML = content;
    modalTag.innerHTML = tag;
    noteId = id;
  }
}

// When the user clicks on <span> (x), close the modal
for (let span of spans) {
  span.onclick = () => {
    modal.style.display = "none";
  }
}

modalUpdateButton.onclick = () => {
  modalUpdateButton.setAttribute("value", `id=${noteId}&title=${modalTitle.value}&content=${modalContent.value}&tag_id=${modalTag.value}`);
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});
