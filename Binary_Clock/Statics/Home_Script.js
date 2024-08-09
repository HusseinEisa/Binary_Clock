document.addEventListener('DOMContentLoaded', function() {
    const formatSelect = document.getElementById('format');
    const timeDiv = document.getElementById('Time');
    const periodDiv = document.getElementById('Period');
    const timeInput = document.getElementById('time');
    const submitBtn = document.getElementById('submitBtn');
    const periodSelect = document.getElementById('period');

    formatSelect.addEventListener('change', function() {
        if (this.value !== 'None') {
            timeDiv.style.display = 'block';
            timeInput.value = ''; // Clear time input when format changes
        } else {
            timeDiv.style.display = 'none';
            periodDiv.style.display = 'none';
            submitBtn.style.display = 'none';
        }
        updateSubmitButtonVisibility();
    });

    timeInput.addEventListener('input', function() {
        const format = formatSelect.value;
        const time = parseInt(this.value);

        if (format === 'decimal' && time > 0 && time < 13 && time <= 24) {
            periodDiv.style.display = 'block';
        } else {
            periodDiv.style.display = 'none';
        }
        updateSubmitButtonVisibility();
    });

    periodSelect.addEventListener('change', updateSubmitButtonVisibility);

    function updateSubmitButtonVisibility() {
        const format = formatSelect.value;
        const time = parseInt(timeInput.value.trim());
        const period = periodSelect.value;

        if (format === 'decimal') {
            if (time > 0 && time < 13) {
                if (period !== "None") {
                    submitBtn.style.display = 'inline-block';
                } else {
                    submitBtn.style.display = 'none';
                }
            } else if (time >= 13 && time <= 24) {
                submitBtn.style.display = 'inline-block';
            } else {
                submitBtn.style.display = 'none';
            }
        } else if (format === 'binary') {
            if (time) {
                submitBtn.style.display = 'inline-block';
            } else {
                submitBtn.style.display = 'none';
            }
        } else {
            submitBtn.style.display = 'none';
        }
    }
});