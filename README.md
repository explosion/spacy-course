# Computational, Interactive and Visual K-12 Math

This repo contains an experimental project developed by Rongpeng(Ron) Li inspired by his tutoring experience at [School On Wheels, Inc](schoolonwheels.org). The ultimate purpose of this project is to develop a full set of K-12 mathematics courses so every kid would have the access to interactive mathematics materials online for free.

The framework for building this website is developed by [Ines Montani](https://github.com/ines). For more information about the technical sides of the framework, please refer to her original [repo](https://github.com/ines/spacy-course).

## 💁 FAQ

**What's the difference between this project and Khan Academy?** Khan Academy is an amazing resource but I think I can do more. There are great benefits to teach with Python. All the course materials, if possible, are developed with Python code. Students can interact with the mathematical concepts and graphs with simple clicks. Beyond that, students will enhance their computational thinking which will benefit them greatly in their future study. 


## 🛣 Roadmap and todos

- [ ] Front-end tests. Also, if someone wants to port this over to TypeScript,
      I'd accept the PR 😛
- [ ] PDF slides. Since the app is using Reveal.js, this should be possible.
- [ ] Testing it for other languages like R. I'd be really curious to see if it
      works. We'd have to adjust the
      [`node.extension` check here](gatsby-node.js) for other files to be
      included via GraphQL.
