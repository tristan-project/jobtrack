document.addEventListener('alpine:init', () => {
    Alpine.data('jobs', () => ({
        jobs: [],
        fetchJobs() {
            fetch('/jobs')
                .then(response => response.json())
                .then(data => this.jobs = data);
        }
    }))
});