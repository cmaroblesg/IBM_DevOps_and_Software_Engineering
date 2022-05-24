<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/IDSNlogo.png" alt="image">{ width=200 height=200 }
    </p>
    <h1>Creating IBM Cloud Functions Entities</h1>
    <p><strong>Estimated time needed:</strong> 45 minutes</p>
    <p>In this lab you will begin creating IBM Cloud Functions entities! You will create and invoke actions and sequences, and you will be encouraged to explore the web action and API management capabilities provided by Cloud Functions. All this will familiarize you with how to start using IBM Cloud Functions yourself.</p>
    <h2>Objectives</h2>
    <p>After completing this lab, you will be able to:</p>
    <ol>
      <li>Create and invoke an action</li>
      <li>Use custom Node.js code for an action</li>
      <li>Create and invoke a sequence</li>
      <li>Enable a web action and access an action using HTTP</li>
      <li>Create an API for your action</li>
    </ol>
    <h2>Exercise 1 : Create and Invoke an Action</h2>
    <p>In this exercise, you will create and invoke your first IBM Cloud Functions action.</p>
    <ol>
      <li>
        <p>Go to the <a href="https://cloud.ibm.com/functions/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMCD0250ENSkillsNetwork23783333-2021-01-01" target="_blank" rel="external">IBM Cloud Functions UI</a>.</p>
      </li>
      <li>
        <p>Click <strong>Start Creating</strong>.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/start_creating.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol>
      <li>
        <p>Click <strong>Action</strong> in order to create an action.</p>
      </li>
      <li>
        <p>Name your action <strong>hello</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Create Package</strong> in order to put this action into a package.</p>
      </li>
      <li>
        <p>Name the package <strong>strings</strong> since we'll make several actions that perform string manipulation.</p>
      </li>
      <li>
        <p>Click <strong>Create</strong>.</p>
      </li>
      <li>
        <p>Choose a Node.js runtime.</p>
      </li>
      <li>
        <p>Click <strong>Create</strong>.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/create_action.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <p>Now you have created an action! Your newly created action should be pre-populated with Node.js code to return a hello world message.</p>
    <ol>
      <li>Click <strong>Invoke</strong>.</li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/invoke_action.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <p>The activations should appear in a panel on the right. Wait for a second and the results should appear within your activation.</p>
    <h2>Exercise 2 : Create a Second Action</h2>
    <p>In this exercise you will create a second action that performs a slightly more advanced task.</p>
    <ol>
      <li>Click <strong>Actions</strong> in the breadcrumbs on the top right to return to the actions page. When it loads, you should see your <strong>strings</strong> package with your <strong>echo</strong> action in it.</li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/actions_breadcrumbs.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="2">
      <li>
        <p>Click <strong>Create</strong> and then <strong>Action</strong> to create another action.</p>
      </li>
      <li>
        <p>Name your action <strong>capitalize</strong>.</p>
      </li>
      <li>
        <p>Select <strong>strings</strong> as the enclosing package.</p>
      </li>
      <li>
        <p>Choose a Node.js runtime.</p>
      </li>
      <li>
        <p>Click <strong>Create</strong>.</p>
      </li>
      <li>
        <p>Use the following code for the main function in the code editor.</p>
        <pre><code class="hljs language-js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params">params</span>) </span>{
  <span class="hljs-keyword">return</span> { <span class="hljs-attr">message</span>: params.message.toUpperCase() };
}
</code></pre>
      </li>
      <li>
        <p>Click <strong>Save</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Invoke with parameters</strong>.</p>
      </li>
      <li>
        <p>Put the following in the input box:</p>
        <pre><code class="hljs language-json">{
  <span class="hljs-attr">"message"</span>: <span class="hljs-string">"I'm hungry!"</span>
}
</code></pre>
      </li>
      <li>
        <p>Click <strong>Apply</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Invoke</strong>.</p>
      </li>
      <li>
        <p>Check the activation results to see your message capitalized.</p>
      </li>
    </ol>
    <h2>Exercise 3 : Create and Invoke a Sequence</h2>
    <p>In this exercise you will create a sequence using your two previously created actions. You'll then invoke the sequence.</p>
    <ol>
      <li>
        <p>Click <strong>Actions</strong> in the breadcrumbs on the top right to return to the actions page. When it loads, you should see your <strong>strings</strong> package with your <strong>hello</strong> action in it.</p>
      </li>
      <li>
        <p>Click <strong>Create</strong> and then <strong>Sequence</strong>.</p>
      </li>
      <li>
        <p>Name the sequence <strong>hello_capitalize</strong>.</p>
      </li>
      <li>
        <p>Select <strong>strings</strong> as the enclosing package.</p>
      </li>
      <li>
        <p>Select an existing action for this sequence and choose <strong>strings / hello</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Create</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Add +</strong> to add another action to this sequence.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/add_to_sequence.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="8">
      <li>
        <p>Click <strong>Select Existing</strong> and choose <strong>strings / capitalize</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Add</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Save</strong> to save the sequence.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/save_sequence.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="11">
      <li>
        <p>Click <strong>Invoke with parameters</strong>.</p>
      </li>
      <li>
        <p>Put the following in the input box:</p>
        <pre><code class="hljs language-json">{
  <span class="hljs-attr">"text"</span>: <span class="hljs-string">"Testing my sequence."</span>
}
</code></pre>
      </li>
      <li>
        <p>Click <strong>Apply</strong>.</p>
      </li>
      <li>
        <p>Click <strong>Invoke</strong>.</p>
      </li>
      <li>
        <p>Check the activation record and ensure that the results include this message: "TESTING MY SEQUENCE."</p>
      </li>
    </ol>
    <p>Great job! You passed the provided input to your sequence. This input was echoed, and that output was passed to the capitalize action, which capitalized the whole thing.</p>
    <h2>Exercise 4 : Enable Web Actions</h2>
    <p>In this exercise you will enable a web action so that your action can be called using HTTP.</p>
    <ol>
      <li>From the <strong>string/hello_capitalize</strong> sequence page, click <strong>Endpoints</strong> in the navigation menu.</li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/sequence_endpoints.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="2">
      <li>Click the checkbox for <strong>Enable as Web Action</strong>.</li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/enable_web_action.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="3">
      <li>
        <p>Click <strong>Save</strong>.</p>
      </li>
      <li>
        <p>Copy the <code>curl</code> command located on this page.</p>
      </li>
      <li>
        <p>Open the IBM Cloud Shell at the top right of the cloud console.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/cloud_shell_icon.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="6">
      <li>
        <p>Run <code>ibmcloud iam oauth-tokens</code> to list your IAM tokens for authentication.</p>
      </li>
      <li>
        <p>Copy the bearer token. You can ignore the word "bearer" and just copy the token.</p>
      </li>
      <li>
        <p>Plug the token into the <code>curl</code> command that you copied.</p>
      </li>
      <li>
        <p>In the Cloud Shell, run the <code>curl</code> command with your bearer token plugged in.</p>
      </li>
    </ol>
    <h2>Exercise 5 : API Management</h2>
    <p>In this exercise you will create an API to better manage and invoke your actions.</p>
    <ol>
      <li>
        <p>Return to the main <a href="https://cloud.ibm.com/functions?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMCD0250ENSkillsNetwork23783333-2021-01-01" target="_blank" rel="external">IBM Cloud Functions page</a>.</p>
      </li>
      <li>
        <p>Click <strong>APIs</strong>.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/api_management.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="3">
      <li>
        <p>Click <strong>Create API</strong>.</p>
      </li>
      <li>
        <p>For API name, put <strong>test</strong>. This will also populate the base path.</p>
      </li>
      <li>
        <p>Click <strong>Create operation</strong>.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/create_operation.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="6">
      <li>
        <p>Put <strong>/hello_capitalize</strong> as the path.</p>
      </li>
      <li>
        <p>Use <strong>GET</strong> for the verb, <strong>strings</strong> for the package**, and choose <strong>hello_capitalize</strong> for the action.</p>
      </li>
      <li>
        <p>Click <strong>Create</strong>.</p>
      </li>
      <li>
        <p>Scroll to the bottom and click <strong>Create</strong>.</p>
      </li>
      <li>
        <p>Copy the API route. This is the domain and the base path.</p>
      </li>
    </ol>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%203/images/api_route.png" style="border:1px solid grey;margin-top:10px;margin-bottom:10px">
    <ol start="11">
      <li>Paste the route into your browser and add <code>/hello_capitalize</code> to it. This should look like <code>https://&#x3C;domain>/test/hello_capitalize</code>.</li>
    </ol>
    <p>You should see your capitalized hello world message in your browser!</p>
    <h2>Conclusion</h2>
    <p>In this lab you created your first actions and sequence! You created two actions that can be independently invoked, and you also joined those actions into a sequence that you invoked. You then enabled a web action and invoked the action using HTTP in a terminal. Finally, you created an API to better manage and invoke your actions.</p>
    <h2>Author(s)</h2>
    <p><a href="https://github.com/ajp-io" target="_blank" rel="external">Alex Parker</a></p>
    <h2></h2>
    <h3 align="center">© IBM Corporation 2020. All rights reserved.</h3>
    <h3></h3>
    <script>window.addEventListener('load', function() {
snFaculty.inject();
});</script>
    <script src="https://skills-network-assets.s3.us.cloud-object-storage.appdomain.cloud/scripts/inject.43989f87.js"></script>
    <script src="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/highlight.min.js"></script>
    <script src="https://unpkg.com/highlightjs-badge@0.1.9/highlightjs-badge.min.js"></script>
  </body>
</html>
