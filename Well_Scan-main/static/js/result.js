const negativeButton = document.getElementById('negative-button');
const positiveButton = document.getElementById('positive-button');
const negativeSection = document.getElementById('negative-section');
const positiveSection = document.getElementById('positive-section');

function showSection(showElement, hideElement) {
    showElement.classList.remove('hidden');
    hideElement.classList.add('hidden');
}

negativeButton.addEventListener('click', () => {
    showSection(negativeSection, positiveSection);
});

positiveButton.addEventListener('click', () => {
    showSection(positiveSection, negativeSection);
});
