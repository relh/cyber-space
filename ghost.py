<!DOCTYPE html>
<html lang="en">
    <head>
        <meta name="robots" content="follow, all" />
        <meta name="description" content="ghost.py" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width = device-width" />
        <title>ghost.py</title>
        <link rel="stylesheet" href="static/normalize.css" type="text/css">
        <link rel="stylesheet" href="static/style.css" type="text/css">
        <link rel="stylesheet" href="static/highlight-theme.css" type="text/css">
        <!--[if lte IE 8]>
            <script src="static/html5-ie.js" type="text/javascript"></script>
        <![endif]-->
    </head>
    <body>
        <header id="intro">
            <h1><a href="#intro">ghost.py</a></h1>
            <p>ghost.py is a webkit web client written in python.</p>
            <code class="python">from ghost import Ghost
ghost = Ghost()
page, extra_resources = ghost.open("http://jeanphi.fr")
assert page.http_status==200 and 'jeanphix' in ghost.content</code>
        </header>
        <section>
            <h1 id="installation"><a href="#installation">Installation</a></h1>
            <p>First you need to install either <a href="http://www.riverbankcomputing.co.uk/software/pyqt/intro" title="PyQt homepage">PyQt</a> or <a href="http://www.pyside.org/" title="PySide homepage">PySide</a> that are availables for many platforms.</p>
            <p>Then you may install ghost.py using pip:</p>
            <pre>pip install Ghost.py</pre>
        </section>
        <section>
            <h1 id="browsing"><a href="#browsing">Browsing</a></h1>
            <article>
                <h1 id="quick-start"><a href="#quick-start">Quick start</a></h1>
                <p>First of all, you need a instance of Ghost web client:</p>
                <code class="python">from ghost import Ghost
ghost = Ghost()</code>
            </article>
            <article>
                <h1 id="open"><a href="#open">Open a web page</a></h1>
                <p>Ghost provide a method that open web page the following way:</p>
                <code class="python">page, resources = ghost.open('http://my.web.page')</code>
                <p>This method returns a tuple of main resource (web page) and all loaded resources (such as CSS files, javascripts, images...).</p>
                <p>All those resources are backed as HttpResource objects.</p>
                <p>At the moment Httpresource objects provide the following attributes:</p>
                <ul>
                    <li><strong>url</strong>: The resource url.</li>
                    <li><strong>http_status</strong>: The HTTP response status code.</li>
                    <li><strong>headers</strong>: The response headers as a dict.</li>
                </ul>
            </article>
            <article>
                <h1 id="javascript"><a href="#javascript">Execute javascript</a></h1>
                <p>Executing javascripts inside webkit frame is one of the most interesting features provided by Ghost:</p>
                <code class="python">result, resources = ghost.evaluate(
    "document.getElementById('my-input').getAttribute('value');")</code>
                <p>The return value is a tuple of:</p>
                <ul>
                    <li>last javascript last statement result.</li>
                    <li>loaded resources (e.g.: when an XHR is fired up).</li>
                </ul>
                <p>As many other Ghost methods, you can pass an extra parameter that tells Ghost you expect a page loading:</p>
                <code class="python">page, resources = ghost.evaluate(
    "document.getElementById('link').click();", expect_loading=True)</code>
                <p>Then the result tuple wil be the same as the one returned by Ghost.open().</p>
            </article>
            <article>
                <h1 id="form"><a href="#form">Play with forms</a></h1>

                <h2>Fill a field</h2>
                <p>You can set a form field value trougth Ghost.set_field_value(selector, value, blur=True, expect_loading=False):</p>
                <code class="python">result, resources = ghost.set_field_value("input[name=username]", "jeanphix")</code>
                <p>If you set optional parameter `blur` to False, the focus will be left on the field (usefull for autocomplete tests).</p>
                <p>For filling file input field, simply pass file path as `value`.</p>
                <h2>Fill an entire form</h2>
                <p>You can fill entire form trougth Ghost.fill(selector, values, expect_loading=False):</p>
                <code class="python">result, resources = ghost.fill("form", {
    "username": "jeanphix",
    "password": "mypassword"
})</code>
                <h2>Submit the form</h2>
                <p>Yon can submit the form by firing `submit` event:</p>
                <code class="python">page, resources = ghost.fire_on("form", "submit", expect_loading=True)</code>
            </article>
            <article>
                <h1 id="waiter"><a href="#waiter">Waiters</a></h1>
                <p>Ghost provides several methods for waiting for specific things before the script continue execution:</p>
                <h2>wait_for_alert()</h2>
                <p> That wait until a javascript alert() is send.</p>
                <code class="python">result, resources = ghost.wait_for_alert()</code>
                <h2>wait_for_page_loaded()</h2>
                <p> That wait until a new page is loaded.</p>
                <code class="python">page, resources = ghost.wait_for_page_loaded()</code>
                <h2>wait_for_selector(selector)</h2>
                <p> That wait until a element match the given selector.</p>
                <code class="python">result, resources = ghost.wait_for_selector("ul.results")</code>
                <h2>wait_for_text(text)</h2>
                <p> That wait until the given text exists inside the frame.</p>
                <code class="python">result, resources = ghost.wait_for_selector("My result")</code>
            </article>
            <article>
                <h1 id="confirm"><a href="#confirm">Confirm</a></h1>
                <p>Accept or deny javascript confirm is quite easy:</p>
                <code class="python">with Ghost.confirm():
    # The confirm() box fired up by click will be accepted
    self.ghost.click('#confirm-button')

with Ghost.confirm(False):
    # The confirm() box fired up by click will be denied
    self.ghost.click('#confirm-button')</code>
            </article>
            <article>
                <h1 id="prompt"><a href="#prompt">Prompt</a></h1>
                <p>Filling a value in prompt box:</p>
                <code class="python">with Ghost.prompt('my value'):
    # prompt() box fired up by click will be filled with 'my value'
    self.ghost.click('#prompt-button')</code>
            </article>
            <article>
                <h1 id="capture"><a href="#capture">Capture viewport</a></h1>
                <p>Ghost.capture_to(path, region=None, selector=None) method let's you take webkit current frame screenshots.</p>
                <p>If you need to capture a specific region of the viewport, just provide a selector (or coordinates tuple) that feets your needs:</p>
                <code class="python">ghost.capture_to('header.png', selector="header")</code>
            </article>
            <section>
                <h1 id="test"><a href="#test">Test client</a></h1>
                <article>
                    <h1 id="wsgi"><a href="#wsgi">WSGI apps</a></h1>
                    <p>Requirements:</p>
                    <pre>pip install tornado</pre>
                    <p>ghost.py provides a simple GhostTestCase that deals with WSGI applications:</p>
                    <code class="python">import unittest
from flask import Flask
from ghost import GhostTestCase


app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'


class MyTest(GhostTestCase):
    port = 5000

    @classmethod
    def create_app(cls):
        return app

    def test_open_home(self):
        self.ghost.open("http://localhost:%s/" % self.port)
        self.assertEqual(self.ghost.content, 'hello world')


if __name__ == '__main__':
    unittest.main()</code>
                    <h2>Debug your test</h2>
                    <p>Tests can be run with a UI by setting display class member to True:</p>
                    <code class="python">class MyTest(GhostTestCase):
    display = True</code>
                </article>
            </section>
            <article>
                <h1 id="sample"><a href="#sample">Sample use case</a></h1>
                <p>The following test tries to center <a href="http://www.openstreetmap.org/" title="OpenStreetMap">http://www.openstreetmap.org/</a> map to France:</p>
                <code class="python"># Opens the web page
ghost.open('http://www.openstreetmap.org/')
# Waits for form search field
ghost.wait_for_selector('input[name=query]')
# Fills the form
ghost.fill("#search_form", {'query': 'France'})
# Submits the form
ghost.fire_on("#search_form", "submit")
# Waits for results (an XHR has been called here)
ghost.wait_for_selector(
    '#search_osm_nominatim .search_results_entry a')
# Clicks first result link
ghost.click(
    '#search_osm_nominatim .search_results_entry:first-child a')
# Checks if map has moved to expected latitude
lat, resources = ghost.evaluate("map.center.lat")
assert float(lat.toString()) == 5860090.806537</code>
            </article>
            <article>
                <h1 id="django"><a href="#django">Django</a></h1>
                <p>Ghost provides an extension for django built on to of the upcoming <a href="https://github.com/django/django/blob/master/django/test/testcases.py#L947">LiveServerTestCase</a>.</p>
                <code class="python">from ghost.ext.django.test import GhostTestCase</code>
            </article>
        </section>
        <section>
            <h1 id="credits"><a href="#credits">Credits</a></h1>
            <ul>
                <li><a href="http://nicolas.perriault.net" title="nicolas perriault">n1k0</a> for <a href="http://n1k0.github.com/casperjs/" title="Casper.js">Casper.js</a> and many helps.</li>
                <li><a href="http://traviscline.com/blog" title="Travis Cline">traviscline</a> for PySide support.</li>
            </ul>
        </section>
        <aside>
            <h1><a href="#navigation" accesskey="n">navigation</a></h1>
            <nav id="navigation" role="navigation">
                <ul>
                    <li><a href="#intro">introduction</a>
                    <li><a href="#installation">installation</a></li>
                    <li><a href="#browsing">browsing</a>
                        <ul>
                            <li><a href="#quick-start">quick start</a></li>
                            <li><a href="#open">open a web page</a></li>
                            <li><a href="#javascript">execute javascript</a></li>
                            <li><a href="#form">forms</a></li>
                            <li><a href="#waiter">waiters</a></li>
                            <li><a href="#confirm">confirm</a></li>
                            <li><a href="#prompt">prompt</a></li>
                            <li><a href="#capture">capture</a></li>
                        </ul>
                    </li>
                    <li><a href="#test">tests</a>
                        <ul>
                            <li><a href="#wsgi">WSGI</a></li>
                            <li><a href="#sample">sample</a></li>
                            <li><a href="#django">django</a></li>
                        </ul>
                    </li>
                    <li><a href="#credits">credits</a></li>
                </ul>
            </nav>
        </aside>
        <footer>
        <p>brought to you by <a href="http://www.jeanphi.fr" title="jean-philippe serafin">jeanphix</a> under MIT license</p>
        <p><a href="http://travis-ci.org/jeanphix/Ghost.py"><img src="https://secure.travis-ci.org/jeanphix/Ghost.py.png" alt="build status" /></a></p>
        <a href="http://github.com/jeanphix/Ghost.py">
            <img style="position: absolute; top: 0; left: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_left_darkblue_121621.png" alt="Fork me on GitHub" />
        </a>
        </footer>
        <script type="text/javascript" src="static/highlight.pack.js"></script>
        <script type="text/javascript"  src="static/site.js">
        </script>
    </body>
</html>
