
            // JavaScript to toggle the status dropdown
            
        
          const statusDropdownButton = document.getElementById('statusDropdownButton');
          const statusDropdown = document.getElementById('statusDropdown');
      
      
          function toggleStatusDropdown() {
              statusDropdown.classList.toggle("hidden");
          }
      
          // Event listener to open/close the dropdown when the button is clicked
          statusDropdownButton.addEventListener("click", toggleStatusDropdown);
      
          // Event listener to close the dropdown when clicking outside of it
          document.addEventListener("click", function (event) {
              if (!statusDropdownButton.contains(event.target) && !statusDropdown.contains(event.target)) {
                  statusDropdown.classList.add("hidden");
              }
          });
      
          
          const priorityDropdownButton = document.getElementById("priorityDropdownButton");
          const priorityDropdown = document.getElementById("priorityDropdown");
      
          // Function to toggle the dropdown's visibility
          function togglePriorityDropdown() {
              priorityDropdown.classList.toggle("hidden");
          }
      
          // Event listener to open/close the dropdown when the button is clicked
          priorityDropdownButton.addEventListener("click", togglePriorityDropdown);
      
          // Event listener to close the dropdown when clicking outside of it
          document.addEventListener("click", function (event) {
              if (!priorityDropdownButton.contains(event.target) && !priorityDropdown.contains(event.target)) {
                  priorityDropdown.classList.add("hidden");
              }
          });
      
          const commentButton = document.getElementById("commentButton");
          const commentPopover = document.getElementById("commentPopover");
      
          // Function to toggle the popover's visibility
          function toggleCommentPopover() {
              commentPopover.classList.toggle("hidden");
          }
      
          // Event listener to open/close the popover when the button is clicked
          commentButton.addEventListener("click", toggleCommentPopover);
      
          // Event listener to close the popover when clicking outside of it
          document.addEventListener("click", function (event) {
              if (!commentButton.contains(event.target) && !commentPopover.contains(event.target)) {
                  commentPopover.classList.add("hidden");
              }
          });
      
          // JavaScript to add a new comment
          const addCommentButton = document.getElementById("addCommentButton");
          const newCommentField = document.getElementById("newComment");
      
          addCommentButton.addEventListener("click", function () {
              const newCommentText = newCommentField.value;
              if (newCommentText.trim() !== "") {
                  // Add the new comment to the list of existing comments
                  const commentList = document.querySelector(".px-4.py-2.border-b.border-gray-300");
                  const newCommentElement = document.createElement("p");
                  newCommentElement.textContent = newCommentText;
                  newCommentElement.className = "text-gray-600";
                  commentList.appendChild(newCommentElement);
      
                  // Clear the new comment text field
                  newCommentField.value = "";
              }
          });