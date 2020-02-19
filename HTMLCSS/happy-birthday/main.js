const topCard = document.getElementById("top");
const cardObject = document.getElementById("card-object");
const openButton = document.getElementById("open-btn");
const closeButton = document.getElementById("close-btn");
let cardOpened = false;

topCard.addEventListener("transitionend", function(event) {
  cardObject.classList.remove("back");
});

cardObject.addEventListener("transitionend", function(event) {
  if (cardOpened) {
    topCard.classList.add("open");
  } else {
    topCard.classList.remove("open");
  }
});

openButton.addEventListener("click", function(event) {
  cardOpened = true;
  cardObject.classList.add("back");
});

closeButton.addEventListener("click", function(event) {
  cardOpened = false;
  cardObject.classList.add("back");
});
