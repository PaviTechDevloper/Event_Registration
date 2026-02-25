const form = document.getElementById("form");
const list = document.getElementById("list");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        department: document.getElementById("department").value,
        age: document.getElementById("age").value,
        phone: document.getElementById("phone").value,
        email: document.getElementById("email").value,
        event_type: document.getElementById("event_type").value
    };

    await fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    alert("Registered Successfully!");
    loadData();
});

async function loadData() {
    const res = await fetch("http://127.0.0.1:5000/registrations");
    const data = await res.json();

    list.innerHTML = "";

    data.forEach(user => {
        list.innerHTML += `
            <p>
                <b>${user.name}</b> - ${user.department} - ${user.event_type}
            </p>
        `;
    });
}

loadData();