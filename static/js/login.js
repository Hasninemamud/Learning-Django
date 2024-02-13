
        function login() {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Simple validation (for demonstration purposes)
            if (username === 'demo' && password === 'password') {
                alert('Login successful!');
            } else {
                alert('Invalid username or password. Please try again.');
            }
        }
