## How to Submit

<div class="alert alert-primary" data-alert="primary" role="alert"><p><strong>You must complete all three steps!</strong></p></div>

#### Step 1 of 3

Create a short video (that’s no more than 3 minutes in length) in which you present your project to the world. Your video **must** begin with an opening section that displays:

- your project’s title;
- your name;
- your GitHub and edX usernames;
- your city and country;
- and, the date you have recorded this video.

It should then go on to demonstrate your project in action, as with slides, screenshots, voiceover, and/or live action. See [howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) for tips on how to make a “screencast,” though you’re welcome to use an actual camera. Upload your video to YouTube (or, if blocked in your country, a similar site) and take note of its URL; it’s fine to flag it as “unlisted,” but don’t flag it as “private.”

Submit [this form](https://forms.cs50.io/d5009db5-ee7d-43f1-8214-87cebc1a554f)!

#### Step 2 of 3

Create a `README.md` text file (named exactly that!) in your `project` folder that explains your project. This file should include your Project Title, the URL of your video (created in step 1 above) and a description of your project. You may use the below as a template.

    # YOUR PROJECT TITLE
    #### Video Demo:  <URL HERE>
    #### Description:
    TODO

If unfamiliar with Markdown syntax, you might find GitHub’s [Basic Writing and Formatting Syntax](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax) helpful. You can also preview your `.md` file by clicking the ‘preview’ icon as explained here: [Markdown Preview in vscode](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview). Standard software project `README`s can often run into the thousands or tens of thousands of words in length; yours need not be that long, but should at least be several hundred words that describe things in detail!

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Your <code class="language-plaintext highlighter-rouge">README.md</code> file should be minimally multiple paragraphs in length, and should explain what your project is, what each of the files you wrote for the project contains and does, and if you debated certain design choices, explaining why you made them. Ensure you allocate sufficient time and energy to writing a <code class="language-plaintext highlighter-rouge">README.md</code> that documents your project thoroughly. Be proud of it! A <code class="language-plaintext highlighter-rouge">README.md</code> in the neighborhood of 750 words is likely to be sufficient for describing your project and all aspects of its functionality. If unable to reach that threshold, that probably means your project is insufficiently complex.</p></div>

Execute the `submit50` command below from within your `project` directory (or from whichever directory contains `README.md` file and your project’s code, which must also be submitted), logging in with your GitHub username and password when prompted. For security, you’ll see asterisks instead of the actual characters in your password.

    submit50 cs50/problems/2024/x/project

<details><summary>Trouble Submitting?</summary><p>If you encounter issues because your project is too large, try to ZIP all of the contents of that directory (except for <code class="language-plaintext highlighter-rouge">README.md</code>) and then submit that instead. If still too large, try removing certain configuration files, reducing the size of your submission below 100MB, or try to upload directly <a href="https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/adding-a-file-to-a-repository">using GitHub’s web interface</a> by visiting <a href="https://github.com/me50/USERNAME">github.com/me50/USERNAME</a> (where <code class="language-plaintext highlighter-rouge">USERNAME</code> is your own GitHub username) and manually dragging and dropping folders, ensuring that when uploading you are doing so to your <code class="language-plaintext highlighter-rouge">cs50/problems/2024/x/project</code> branch, otherwise the system will not be able to check it!</p></details>

#### Step 3 of 3

Be sure to visit your gradebook at [cs50.me/cs50x](https://cs50.me/cs50x) a few minutes after you submit. It’s only by loading your Gradebook that the system can check to see whether you have completed the course, and that is also what triggers the (instant) generation of your free CS50 Certificate and the (within 30 days) generation of the Verified Certificate from edX, if you’ve completed all of the other assignments. Be sure to claim your free certificate (by following the link at the top of your gradebook) before 1 January 2025.

<div class="alert alert-danger" data-alert="danger" role="alert"><p>Don’t skip the above step! The course is not considered complete until you do the above and see the green banner saying you’ve completed the course. If you do not do the above prior to 1 January 2025, your status in the course will be subject to the <a href="../faqs/#deadlines" class="alert-link">carryover rules</a> in the FAQ. The staff will not make any manual corrections in early 2025 based on this being skipped!</p></div>

That’s it! Your project should be graded within a few minutes. If you don’t see any results in your gradebook, best to resubmit (running the above `submit50` command) with only your README.md file this time. No need to resubmit your form.

This was CS50x!
