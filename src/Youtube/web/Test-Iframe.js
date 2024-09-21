// Create the IFrame element
const iframe = document.createElement('iframe');

// YouTube video URL
iframe.src = "https://www.youtube.com/embed/SB-qEYVdvXA";

// IFrame attributes
iframe.width = "560";
iframe.height = "315";
iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
iframe.allowFullscreen = true;

// Optional styling
iframe.style.position = "relative";
iframe.style.top = "10px";
iframe.style.right = "10px";
iframe.style.zIndex = "1000";

// Append the IFrame
document.body.appendChild(iframe);