const grid = document.getElementById("cardGrid");
const modal = document.getElementById("modal");
const searchInput = document.getElementById("searchInput");
const savedBtn = document.getElementById("savedBtn");
const difficultyFilter = document.getElementById("difficultyFilter");
const difficultyTrigger = document.getElementById("difficultyTrigger");
const difficultyPanel = document.getElementById("difficultyPanel");
const newCakeBtn = document.getElementById("newCakeBtn");
const newCakeModal = document.getElementById("newCakeModal");
const newCakeClose = document.querySelector(".new-cake-close");
const saveNewCakeBtn = document.getElementById("saveNewCakeBtn");
const editCakeBtn = document.getElementById("editCakeBtn");
const deleteCakeBtn = document.getElementById("deleteCakeBtn");
const noticeBar = document.getElementById("noticeBar");
const confirmDeleteModal = document.getElementById("confirmDeleteModal");
const confirmDeleteOk = document.getElementById("confirmDeleteOk");
const confirmDeleteCancel = document.getElementById("confirmDeleteCancel");

let editingCakeId = null;
let noticeTimeoutId = null;

const SAVED_KEY = "savedCakes";

let currentCakes = [];

function getSavedIds() {
    try {
        return JSON.parse(localStorage.getItem(SAVED_KEY) || "[]");
    } catch {
        return [];
    }
}

function toggleSaved(cakeId) {
    const ids = getSavedIds();
    const i = ids.indexOf(cakeId);
    if (i >= 0) ids.splice(i, 1);
    else ids.push(cakeId);
    localStorage.setItem(SAVED_KEY, JSON.stringify(ids));
}

function isSaved(cakeId) {
    return getSavedIds().includes(cakeId);
}

function showError(msg) {
    if (grid) grid.innerHTML = `<p class='empty-msg'>${msg}</p>`;
}

function showNotice(msg) {
    if (!noticeBar) return;
    noticeBar.textContent = msg;
    noticeBar.classList.remove("hidden");
    if (noticeTimeoutId) clearTimeout(noticeTimeoutId);
    noticeTimeoutId = setTimeout(() => {
        noticeBar.classList.add("hidden");
    }, 3000);
}

function loadCakes() {
    fetch("/api/cakes")
        .then(res => res.ok ? res.json() : Promise.reject(new Error("API error")))
        .then(data => {
            currentCakes = Array.isArray(data) ? data : [];
            applyFiltersAndRender();
        })
        .catch(() => showError("Failed to load cakes. Is the server running?"));
}

function goHome() {
    if (searchInput) searchInput.value = "";
    loadCakes();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function showSavedCakes() {
    const ids = getSavedIds();
    if (ids.length === 0) {
        showError("No saved cakes yet. Heart your favorites!");
        return;
    }
    fetch("/api/cakes")
        .then(r => r.ok ? r.json() : [])
        .then(all => {
            const arr = Array.isArray(all) ? all : [];
            const saved = arr.filter(c => ids.includes(c._id));
            if (saved.length === 0) {
                showError("No saved cakes found.");
            } else {
                currentCakes = saved;
                applyFiltersAndRender();
            }
        })
        .catch(() => showError("Failed to load saved cakes."));
}

function doSearch() {
    const query = searchInput ? searchInput.value.trim() : "";
    if (!query) {
        loadCakes();
        return;
    }
    fetch(`/api/search?q=${encodeURIComponent(query)}`)
        .then(res => res.ok ? res.json() : [])
        .then(results => {
            const arr = Array.isArray(results) ? results : [];
            currentCakes = arr;
            if (currentCakes.length === 0) {
                showError("No cakes found. Try another search!");
            } else {
                applyFiltersAndRender();
            }
        })
        .catch(() => showError("Search failed."));
}

function applyFiltersAndRender() {
    if (!grid) return;
    const level = difficultyFilter ? difficultyFilter.value : "";
    let toShow = currentCakes;
    if (level) {
        toShow = toShow.filter(c => c.difficulty === level);
    }
    renderCards(toShow);
}

function renderCards(cakes) {
    if (!grid) return;
    grid.innerHTML = "";
    const arr = Array.isArray(cakes) ? cakes : [];
    arr.forEach(cake => {
        const card = document.createElement("div");
        card.className = "card";
        const saved = isSaved(cake._id);
        card.innerHTML = `
            <button class="heart-btn ${saved ? "saved" : ""}" data-cake-id="${cake._id}" title="Save cake" aria-label="Save cake">${saved ? "♥" : "♡"}</button>
            <img src="${cake.image}" alt="${cake.name}">
            <div class="card-title">${cake.name}</div>
        `;
        card.addEventListener("click", (e) => {
            if (e.target.closest(".heart-btn")) return;
            openModal(cake);
        });
        const heartBtn = card.querySelector(".heart-btn");
        heartBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            toggleSaved(cake._id);
            heartBtn.classList.toggle("saved");
            heartBtn.textContent = heartBtn.classList.contains("saved") ? "♥" : "♡";
        });
        grid.appendChild(card);
    });
}

function openModal(cake) {
    document.getElementById("modalImage").src = cake.image;
    document.getElementById("modalName").textContent = cake.name;
    document.getElementById("modalDesc").textContent = cake.description;

    const ingList = document.getElementById("modalIngredients");
    ingList.innerHTML = cake.ingredients.map(i => `<li>${i}</li>`).join("");

    const stepList = document.getElementById("modalSteps");
    stepList.innerHTML = cake.steps.map(s => `<li>${s}</li>`).join("");

    modal.classList.remove("hidden");

    // Remember which cake is open for edit/delete actions
    modal.dataset.cakeId = cake._id;
    modal.dataset.cakeJson = JSON.stringify(cake);
}

// Load all cakes on page load
window.addEventListener("DOMContentLoaded", loadCakes);

// Search (Enter key only)
if (searchInput) searchInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") doSearch();
});

if (savedBtn) savedBtn.addEventListener("click", showSavedCakes);
if (difficultyFilter) difficultyFilter.addEventListener("change", applyFiltersAndRender);

// Custom difficulty dropdown
if (difficultyTrigger && difficultyPanel) {
    difficultyTrigger.addEventListener("click", (e) => {
        e.stopPropagation();
        const open = difficultyPanel.classList.toggle("hidden");
        difficultyTrigger.setAttribute("aria-expanded", !open);
    });
    difficultyPanel.querySelectorAll(".difficulty-option").forEach(opt => {
        opt.addEventListener("click", () => {
            const value = opt.getAttribute("data-value") || "";
            const label = opt.textContent.trim();
            if (difficultyFilter) {
                difficultyFilter.value = value;
                difficultyFilter.dispatchEvent(new Event("change", { bubbles: true }));
            }
            difficultyTrigger.textContent = label;
            difficultyPanel.classList.add("hidden");
            difficultyTrigger.setAttribute("aria-expanded", "false");
        });
    });
    document.addEventListener("click", () => {
        difficultyPanel.classList.add("hidden");
        difficultyTrigger.setAttribute("aria-expanded", "false");
    });
}

// Add-cake modal
function resetAddCakeForm() {
    document.getElementById("newName").value = "";
    document.getElementById("newImage").value = "";
    const imageFileInput = document.getElementById("newImageFile");
    if (imageFileInput) imageFileInput.value = "";
    document.getElementById("newCategory").value = "";
    document.getElementById("newDifficulty").value = "Easy";
    document.getElementById("newPrep").value = "";
    document.getElementById("newBake").value = "";
    document.getElementById("newServings").value = "";
    document.getElementById("newDescription").value = "";
    document.getElementById("newIngredients").value = "";
    document.getElementById("newSteps").value = "";
    editingCakeId = null;
    if (saveNewCakeBtn) saveNewCakeBtn.textContent = "Save Cake";
}

if (newCakeBtn && newCakeModal) {
    newCakeBtn.addEventListener("click", () => {
        resetAddCakeForm();
        newCakeModal.classList.remove("hidden");
    });
}
if (newCakeClose && newCakeModal) {
    newCakeClose.addEventListener("click", () => {
        newCakeModal.classList.add("hidden");
        editingCakeId = null;
        saveNewCakeBtn.textContent = "Save Cake";
    });
}
if (saveNewCakeBtn && newCakeModal) {
    saveNewCakeBtn.addEventListener("click", () => {
        const name = document.getElementById("newName").value.trim();
        const imageUrl = document.getElementById("newImage").value.trim();
        const imageFileInput = document.getElementById("newImageFile");
        const category = document.getElementById("newCategory").value.trim();
        const difficulty = document.getElementById("newDifficulty").value;
        const prep_time = document.getElementById("newPrep").value.trim();
        const bake_time = document.getElementById("newBake").value.trim();
        const servings = Number(document.getElementById("newServings").value) || 0;
        const description = document.getElementById("newDescription").value.trim();
        const ingredients = document.getElementById("newIngredients").value
            .split("\n").map(s => s.trim()).filter(Boolean);
        const steps = document.getElementById("newSteps").value
            .split("\n").map(s => s.trim()).filter(Boolean);

        if (!name) {
            alert("Cake name is required.");
            return;
        }

        const url = editingCakeId ? `/api/cakes/${editingCakeId}` : "/api/cakes";
        const method = editingCakeId ? "PUT" : "POST";
        const hasFile = imageFileInput && imageFileInput.files && imageFileInput.files.length > 0;

        let options;
        if (hasFile) {
            const form = new FormData();
            form.append("name", name);
            form.append("image", imageUrl);
            form.append("category", category);
            form.append("difficulty", difficulty);
            form.append("prep_time", prep_time);
            form.append("bake_time", bake_time);
            form.append("servings", String(servings));
            form.append("description", description);
            form.append("ingredients", ingredients.join("\n"));
            form.append("steps", steps.join("\n"));
            form.append("image_file", imageFileInput.files[0]);
            options = { method, body: form };
        } else {
            options = {
                method,
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    name,
                    image: imageUrl,
                    category,
                    difficulty,
                    prep_time,
                    bake_time,
                    servings,
                    description,
                    ingredients,
                    steps
                })
            };
        }

        fetch(url, options)
            .then(res => res.ok ? res.json() : res.json().then(e => Promise.reject(e)))
            .then(() => {
                newCakeModal.classList.add("hidden");
                editingCakeId = null;
                saveNewCakeBtn.textContent = "Save Cake";
                if (imageFileInput) imageFileInput.value = "";
                loadCakes();
            })
            .catch(err => {
                alert(err.error || `Failed to ${method === "POST" ? "add" : "update"} cake`);
            });
    });
}

// Edit / Delete from detail modal
if (editCakeBtn && modal && newCakeModal) {
    editCakeBtn.addEventListener("click", () => {
        const raw = modal.dataset.cakeJson;
        if (!raw) return;
        const cake = JSON.parse(raw);

        // Prefill form fields
        document.getElementById("newName").value = cake.name || "";
        document.getElementById("newImage").value = cake.image || "";
        const imageFileInput = document.getElementById("newImageFile");
        if (imageFileInput) imageFileInput.value = "";
        document.getElementById("newCategory").value = cake.category || "";
        document.getElementById("newDifficulty").value = cake.difficulty || "Easy";
        document.getElementById("newPrep").value = cake.prep_time || "";
        document.getElementById("newBake").value = cake.bake_time || "";
        document.getElementById("newServings").value = cake.servings || "";
        document.getElementById("newDescription").value = cake.description || "";
        document.getElementById("newIngredients").value = (cake.ingredients || []).join("\n");
        document.getElementById("newSteps").value = (cake.steps || []).join("\n");

        editingCakeId = cake._id;
        saveNewCakeBtn.textContent = "Save Changes";

        modal.classList.add("hidden");
        newCakeModal.classList.remove("hidden");
    });
}

function hideConfirmDeleteModal() {
    if (confirmDeleteModal) {
        confirmDeleteModal.classList.add("hidden");
        confirmDeleteModal.style.display = "";
    }
}

function showConfirmDeleteModal() {
    if (confirmDeleteModal) {
        confirmDeleteModal.classList.remove("hidden");
        confirmDeleteModal.style.display = "flex";
    }
}

function performDelete(cakeId) {
    if (!cakeId) return;
    hideConfirmDeleteModal();
    if (modal) modal.classList.add("hidden");
    fetch(`/api/cakes/${cakeId}`, { method: "DELETE" })
        .then(res => res.ok ? res.json() : res.json().then(e => Promise.reject(e)))
        .then(() => {
            showNotice("Cake deleted.");
            loadCakes();
        })
        .catch(err => {
            alert(err && err.error ? err.error : "Failed to delete cake");
        });
}

// Delete button: show custom confirm or fallback to native confirm
if (deleteCakeBtn && modal) {
    deleteCakeBtn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        const cakeId = modal.dataset.cakeId;
        if (!cakeId) return;
        if (confirmDeleteModal) {
            confirmDeleteModal.dataset.pendingDeleteId = cakeId;
            showConfirmDeleteModal();
        } else {
            if (confirm("Delete this cake? This cannot be undone.")) performDelete(cakeId);
        }
    });
}

if (confirmDeleteOk && confirmDeleteModal) {
    confirmDeleteOk.addEventListener("click", (e) => {
        e.preventDefault();
        const cakeId = confirmDeleteModal.dataset.pendingDeleteId;
        hideConfirmDeleteModal();
        if (cakeId) performDelete(cakeId);
    });
}

if (confirmDeleteCancel && confirmDeleteModal) {
    confirmDeleteCancel.addEventListener("click", (e) => {
        e.preventDefault();
        hideConfirmDeleteModal();
    });
}

if (confirmDeleteModal) {
    confirmDeleteModal.addEventListener("click", (e) => {
        if (e.target === confirmDeleteModal) hideConfirmDeleteModal();
    });
}

// Logo click = go home
const logo = document.getElementById("logo");
if (logo) logo.addEventListener("click", goHome);
const logoImg = document.getElementById("logoImg");
if (logoImg) logoImg.addEventListener("click", goHome);

// Close modal
const closeBtn = document.querySelector(".close-btn");
if (closeBtn) closeBtn.addEventListener("click", () => {
    if (modal) modal.classList.add("hidden");
});
if (modal) modal.addEventListener("click", (e) => {
    if (e.target === modal) modal.classList.add("hidden");
});
