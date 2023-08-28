    

        // JavaScript to toggle the status dropdown
const statusDropdownButtons = document.querySelectorAll(".status-dropdown-button");


statusDropdownButtons.forEach(button => {
    button.addEventListener("click", function () {
        const statusDropdown = this.nextElementSibling; // Assumes the dropdown is next sibling
        statusDropdown.classList.toggle("hidden");
        document.addEventListener("click", function (event) {
            if (!button.contains(event.target) && !statusDropdown.contains(event.target)) {
                statusDropdown.classList.add("hidden");
            }
        });
        
    });
    
});

//javascript code to handle priority dropdown
const priorityDropdownButtons = document.querySelectorAll(".priority-dropdown-button");


priorityDropdownButtons.forEach(button => {
    button.addEventListener("click", function () {
        const priorityDropdown = this.nextElementSibling; // Assumes the dropdown is next sibling
        priorityDropdown.classList.toggle("hidden");
        document.addEventListener("click", function (event) {
            if (!button.contains(event.target) && !priorityDropdown.contains(event.target)) {
                priorityDropdown.classList.add("hidden");
            }
        });
        
    });
    
});

//javascript o handle comment dropdown
const commentDropdownButtons = document.querySelectorAll(".comment-dropdown-button");


commentDropdownButtons.forEach(button => {
    button.addEventListener("click", function () {
        const commentDropdown = this.nextElementSibling; // Assumes the dropdown is next sibling
        commentDropdown.classList.toggle("hidden");
        document.addEventListener("click", function (event) {
            if (!button.contains(event.target) && !commentDropdown.contains(event.target)) {
                commentDropdown.classList.add("hidden");
            }
        });
        
    });
    
});

        
 
 // JavaScript to month
    
const prevMonthButton = document.getElementById("prevMonth");
const nextMonthButton = document.getElementById("nextMonth");
const currentMonthYear = document.getElementById("currentMonthYear");
const calendarBody = document.getElementById("calendarBody");

let currentDate = new Date();

function renderCalendar() {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();

    currentMonthYear.textContent = `${new Intl.DateTimeFormat('en-US', { month: 'long' }).format(currentDate)} ${year}`;

    let calendarHTML = "";

    let dayCounter = 1;
    for (let i = 0; i < 6; i++) {
        calendarHTML += "<tr>";
        for (let j = 0; j < 7; j++) {
            if ((i === 0 && j < firstDay.getDay()) || dayCounter > daysInMonth) {
                calendarHTML += "<td class='p-2 mx-4'></td>";
            } else {
                calendarHTML += `<td class="p-2 mx-4">${dayCounter}</td>`;
                dayCounter++;
            }
        }
        calendarHTML += "</tr>";
    }

    calendarBody.innerHTML = calendarHTML;
}

prevMonthButton.addEventListener("click", () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
});

nextMonthButton.addEventListener("click", () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
});

renderCalendar();

