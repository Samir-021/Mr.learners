// Header Scroll
let nav = document.querySelector(".navbar");
window.onscroll = function () {
    if (document.documentElement.scrollTop > 50) {
        nav.classList.add("header-scrolled");
    } else {
        nav.classList.remove("header-scrolled");
    }
};

// Nav hide
let navBar = document.querySelectorAll(".nav-link");
let navCollapse = document.querySelector(".navbar-collapse.collapse");
navBar.forEach(function (a) {
    a.addEventListener("click", function () {
        navCollapse.classList.remove("show");
    });
});

// Swiper Slider
var swiper = new Swiper(".mySwiper", {
    direction: "vertical",
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 3500,
    },
});


// Initialize location variables
let userLat = null;
let userLon = null;
const latInput = document.getElementById("user-lat");
const lonInput = document.getElementById("user-lon");
const form = document.getElementById("search-form");

// Function to update location dynamically
function updateLocation(position) {
    userLat = position.coords.latitude;
    userLon = position.coords.longitude;

    // Update hidden input fields
    latInput.value = userLat;
    lonInput.value = userLon;

    console.log(`User Location Updated: Latitude ${userLat}, Longitude ${userLon}`);
}

// Function to handle errors
function handleLocationError(error) {
    let errorMessage = "Unable to fetch location.";
    if (error.code === error.PERMISSION_DENIED) {
        errorMessage = "Permission to access location was denied.";
    } else if (error.code === error.POSITION_UNAVAILABLE) {
        errorMessage = "Location information is unavailable.";
    } else if (error.code === error.TIMEOUT) {
        errorMessage = "The request to get user location timed out.";
    }

    alert(errorMessage);
    console.error("Geolocation Error:", error);
}

// Initialize location tracking
if (navigator.geolocation) {
    navigator.geolocation.watchPosition(updateLocation, handleLocationError, {
        enableHighAccuracy: true, // Use high accuracy GPS data
        maximumAge: 0,           // Do not use cached location data
        timeout: 5000            // Set timeout for location fetch
    });
} else {
    alert("Geolocation is not supported by your browser.");
}

// Submit the form only if coordinates are set
form.addEventListener("submit", (event) => {
    if (!userLat || !userLon) {
        event.preventDefault(); // Prevent form submission
        alert("Please wait for location to be fetched.");
        return;
    }
    console.log("Form submitted successfully with location data.");
});



