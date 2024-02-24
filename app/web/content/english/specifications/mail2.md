## Specification

Using JavaScript, HTML, and CSS, complete the implementation of your single-page-app email client inside of `inbox.js` (and not additional or other files; for grading purposes, we’re only going to be considering `inbox.js`!). You must fulfill the following requirements:

- **Send Mail**: When a user submits the email composition form, add JavaScript code to actually send the email.
  - You’ll likely want to make a `POST` request to `/emails`, passing in values for `recipients`, `subject`, and `body`.
  - Once the email has been sent, load the user’s sent mailbox.
- **Mailbox**: When a user visits their Inbox, Sent mailbox, or Archive, load the appropriate mailbox.
  - You’ll likely want to make a `GET` request to `/emails/<mailbox>` to request the emails for a particular mailbox.
  - When a mailbox is visited, the application should first query the API for the latest emails in that mailbox.
  - When a mailbox is visited, the name of the mailbox should appear at the top of the page (this part is done for you).
  - Each email should then be rendered in its own box (e.g. as a `<div>` with a border) that displays who the email is from, what the subject line is, and the timestamp of the email.
  - If the email is unread, it should appear with a white background. If the email has been read, it should appear with a gray background.
- **View Email**: When a user clicks on an email, the user should be taken to a view where they see the content of that email.
  - You’ll likely want to make a `GET` request to `/emails/<email_id>` to request the email.
  - Your application should show the email’s sender, recipients, subject, timestamp, and body.
  - You’ll likely want to add an additional `div` to `inbox.html` (in addition to `emails-view` and `compose-view`) for displaying the email. Be sure to update your code to hide and show the right views when navigation options are clicked.
  - See the hint in the Hints section about how to add an event listener to an HTML element that you’ve added to the DOM.
  - Once the email has been clicked on, you should mark the email as read. Recall that you can send a `PUT` request to `/emails/<email_id>` to update whether an email is read or not.
- **Archive and Unarchive**: Allow users to archive and unarchive emails that they have received.
  - When viewing an Inbox email, the user should be presented with a button that lets them archive the email. When viewing an Archive email, the user should be presented with a button that lets them unarchive the email. This requirement does not apply to emails in the Sent mailbox.
  - Recall that you can send a `PUT` request to `/emails/<email_id>` to mark an email as archived or unarchived.
  - Once an email has been archived or unarchived, load the user’s inbox.
- **Reply**: Allow users to reply to an email.
  - When viewing an email, the user should be presented with a “Reply” button that lets them reply to the email.
  - When the user clicks the “Reply” button, they should be taken to the email composition form.
  - Pre-fill the composition form with the `recipient` field set to whoever sent the original email.
  - Pre-fill the `subject` line. If the original email had a subject line of `foo`, the new subject line should be `Re: foo`. (If the subject line already begins with `Re:` , no need to add it again.)
  - Pre-fill the `body` of the email with a line like `"On Jan 1 2020, 12:00 AM foo@example.com wrote:"` followed by the original text of the email.

## Hints

- To create an HTML element and add an event handler to it, you can use JavaScript code like the below:

```
const element = document.createElement('div');
element.innerHTML = 'This is the content of the div.';
element.addEventListener('click', function() {
    console.log('This element has been clicked!')
});
document.querySelector('#container').append(element);
```

This code creates a new `div` element, sets its `innerHTML`, adds an event handler to run a particular function when that `div` is clicked on, and then adds it to an HTML element whose `id` is `container` (this code assumes that there is a HTML element whose `id` is `container`: you’ll likely want to change the argument to `querySelector` to be whichever element you’d like to add an element to).

- You may find it helpful to edit `mail/static/mail/styles.css` to add any CSS you need for the application.
- Recall that if you have a JavaScript array, you can loop over each element of that array using [`forEach`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach).
- Recall that normally, for `POST` and `PUT` requests, Django requires a CSRF token to guard against potential cross-site request forgery attacks. For this project, we’ve intentionally made the API routes CSRF-exempt, so you won’t need a token. In a real-world project, though, always best to guard against such potential vulnerabilities!

## How to Submit

1.  Visit [this link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), log in with your GitHub account, and click **Authorize cs50**. Then, check the box indicating that you’d like to grant course staff access to your submissions, and click **Join course**.
2.  [Install Git](https://git-scm.com/downloads) and, optionally, [install `submit50`](https://cs50.readthedocs.io/submit50/).

<div class="alert alert-success" data-alert="success" role="alert"><p>When you submit your project, the contents of your <code class="language-plaintext highlighter-rouge">web50/projects/2020/x/mail</code> branch should match the file structure of the unzipped distribution code as originally received. That is to say, your files should not be nested inside of any other directories of your own creation. Your branch should also not contain any code from any other projects, only this one. Failure to adhere to this file structure will likely result in your submission being rejected.</p>

<p>By way of example, for this project that means that if the grading staff visits <code class="language-plaintext highlighter-rouge">https://github.com/me50/USERNAME/tree/web50/projects/2020/x/mail</code> (where <code class="language-plaintext highlighter-rouge">USERNAME</code> is your own GitHub username as provided in the form, below) we should see the two subdirectories (<code class="language-plaintext highlighter-rouge">mail</code>, <code class="language-plaintext highlighter-rouge">project3</code>) and the <code class="language-plaintext highlighter-rouge">manage.py</code> file. If that’s not how your code is organized when you check, reorganize your repository needed to match this paradigm.</p></div>

3.  If you’ve installed `submit50`, execute

        submit50 web50/projects/2020/x/mail

    Otherwise, using Git, push your work to `https://github.com/me50/USERNAME.git`, where `USERNAME` is your GitHub username, on a branch called `web50/projects/2020/x/mail`.

4.  [Record a screencast](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) not to exceed 5 minutes in length (and not uploaded more than one month prior to your submission of this project), in which you demonstrate your project’s functionality. Be certain that every element of the specification, above, is demonstrated in your video. There’s no need to show your code in this video, just your application in action; we’ll review your code on GitHub. [Upload that video to YouTube](https://www.youtube.com/upload) (as unlisted or public, but not private) or somewhere else. In your video’s description, you must timestamp where your video demonstrates each of the five (5) elements of the specification. **This is not optional**, videos without timestamps in their description will be automatically rejected.
5.  Submit [this form](https://forms.cs50.io/8f569b7d-bd6d-4446-82ac-d65b86d95bbb).

You can then go to [https://cs50.me/cs50w](https://cs50.me/cs50w) to view your current progress!
