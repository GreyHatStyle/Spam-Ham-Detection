
async function handleFormSubmit(event) {
    event.preventDefault();  
    const inputText = document.getElementById("inputText").value;
    const outputTextarea = document.getElementById("outputTextarea");
    if (inputText === "") {
        alert("Please enter some text.");
        return;
    }
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputText: inputText })
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        outputTextarea.value = data.answer;
    } catch (error) {
        console.error('There was an error:', error);
        outputTextarea.value = "Error fetching response.";
    }
}
document.getElementById("validateButton").addEventListener("click", handleFormSubmit);
