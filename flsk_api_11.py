from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Anupam  | Portfolio</title>
</head>
<body style="font-family: 'Poppins', sans-serif; margin: 0; background-color: #f8f9fa; color: #333;">
    <header style="background-color: #0a192f; color: white; text-align: center; padding: 2rem 1rem;">
    <h1 style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;"> ANUPAM  </h1>
     <nav>
      <ul style="list-style: none; padding: 0; display: flex; justify-content: center; gap: 2rem; margin: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;">
        <li><a href="#about" style="color: white; text-decoration: none; font-weight: bold;">About</a></li>
        <li><a href="#skills" style="color: white; text-decoration: none; font-weight: bold;">Skills</a></li>
        <li><a href="#projects" style="color: white; text-decoration: none; font-weight: bold;">Projects</a></li>
        <li><a href="#contact" style="color: white; text-decoration: none; font-weight: bold;">Contact</a></li>
      </ul>
    </nav>
  </header>

    <section id="about" class="section" style="padding: 3rem 1rem; text-align: center; margin: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;">
  <h2>About Me</h2>
  <p>
    Hi! I'm <strong>ANUPAM</strong>, a B.Tech student and web development enthusiast passionate about building clean, responsive, and user-friendly websites. I love learning new technologies and turning ideas into digital experiences.
  </p>
</section>

    <section id="skills" class="section" style="padding: 3rem 1rem; text-align: center; margin: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;">
  <h2>Skills</h2>
  <ul class="skills-list" style="list-style: none; padding: 0; display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;">
    <li> HTML</li>
    <li> CSS</li>
    <li> JavaScript</li>
    <li> Git & GitHub</li>
  </ul>
</section>

  <section id="projects" class="section" style="padding: 3rem 1rem; text-align: center; margin: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;">
  <h2>My Projects</h2>
  
  <div class="project" style="background: white; padding: 1.5rem; margin: 1rem auto; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
    <h3>Portfolio Website</h3>
    <p>A responsive personal portfolio built using HTML & CSS.</p>
    <a href="#" target="_blank" style="color: #007bff; text-decoration: none;">🔗 Live Demo</a> | 
    <a href="#" target="_blank" style="color: #007bff; text-decoration: none;">💻 View Code</a>
  </div>

  <div class="project" style="background: white; padding: 1.5rem; margin: 1rem auto; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
    <h3>To-Do List App</h3>
    <p>A simple task manager created using HTML, CSS, and JavaScript.</p>
    <a href="#" target="_blank" style="color: #007bff; text-decoration: none;">🔗 Live Demo</a> | 
    <a href="#" target="_blank" style="color: #007bff; text-decoration: none;">💻 View Code</a>
  </div>
</section>

    <section id="contact" class="section" style="padding: 3rem 1rem; text-align: center; margin: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;">
  <h2>Contact</h2>
  <p>Email: <a href="mailto:beinganupam.rky@gmail.com" style="color: #007bff; text-decoration: none;">beinganupam.rky@gmail.com</a></p>
  <p>LinkedIn: <a href="#" target="_blank" style="color: #007bff; text-decoration: none;">linkedin.com/in/anupamyadav</a></p>
  <p>GitHub: <a href="#" target="_blank" style="color: #007bff; text-decoration: none;">github.com/anupamyadav</a></p>
</section>

  <footer style="background-color: #0a192f; color: white; text-align: center; padding: 1rem; margin-top: 2rem;">
  <p style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif;">© 2025 Anupam  | Built with using HTML, CSS & JavaScript</p>
</footer>
</body>
</html>"""

@app.route("/about")
def abouta():
    return """
    <h1>I am about page</h1>
    <h2>I am running in Flask</h2>
    """

if __name__ == "__main__":
    app.run(debug=True)
