window.onload = function initFingerprintJS() {
    // Initialize an agent at application startup.
    fpPromise = FingerprintJS.load()

    var visitorId;
    // Get the visitor identifier when you need it.
    fpPromise
    .then(fp => fp.get())
    .then(result => {
        // This is the visitor identifier:
        visitorId = result.visitorId
        add_payload(visitorId)
    })
}

function add_payload(visitorId){
    quiz_element = document.getElementById('quiz')
    hiddenInput = document.createElement('input');
    hiddenInput.type = 'hidden';
    hiddenInput.name = "visitorId";
    hiddenInput.value = visitorId;
    quiz_element.appendChild(hiddenInput);
}

var changedGroups = []

// Called from the onchange
function countAnswered(groupName){

    // If group name is not in our list
    if(changedGroups.indexOf(groupName) == -1){

        // Add it
        changedGroups.push(groupName)
        console.log("Added group to group list:" + groupName + " total changed groups: " + changedGroups.length)
        updateNumberAnswered(changedGroups.length)
    }
}

var numberAnswered = "0"
var numberTotalAnswers = "10"

function updateNumberAnswered(newNumber){
    firstBold.textContent = newNumber
}

var navbar = document.getElementById('navBar')
var li = document.createElement("li")
li.classList.add("nav-item")
li.id = "questionsCompleted"

var p = document.createElement("p")
p.classList.add("nav-link", "text-light", "fs-3", "me-5", "d-none", "questions-block")

var firstBold = document.createElement("b")
firstBold.textContent = numberAnswered

var secondBold = document.createElement("b")
secondBold.textContent = numberTotalAnswers

p.appendChild(firstBold)
p.appendChild(document.createTextNode(" out of "))
p.appendChild(secondBold)
p.appendChild(document.createTextNode(" questions answered"))

li.appendChild(p)
navbar.insertBefore(li, navbar.firstChild)
