const posts = document.getElementById('posts');

async function postman() {
    const url = "https://jsonplaceholder.typicode.com/posts";
    
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);

        for (let i = 0; i < data.length; i++) {
            const post = data[i];

            const postDiv = document.createElement('div');
            postDiv.classList.add('post');

            postDiv.innerHTML = `
                <h2>User ID: ${post.userId}</h2>
                <h3>Post ID: ${post.id}</h3>
                <h4>Title: ${post.title}</h4>
                <p>${post.body}</p>
            `;
            posts.appendChild(postDiv);
        }
        
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

postman();



