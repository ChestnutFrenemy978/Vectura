document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById("fileInput");
    formData.append("file", fileInput.files[0]);

    const response = await fetch("/upload", { method: "POST", body: formData });
    const data = await response.json();

    if (data.error) {
        alert(data.error);
    } else {
        document.getElementById("result").innerHTML = 
            <a href="/download/${data.result}" download>Download Processed File</a>
        ;
    }
});