## -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>

<%block name="metatitle">Login | ${parent.metatitle()}</%block>

<%block name="topnav"></%block>

<%block name="content">
    <div class="container">
        <form class="form-signin" action="." method="post">
            <h2 class="form-signin-heading">Please sign in</h2>
            <input type="text" name="email" class="input-block-level" placeholder="Email address">
            <input type="password" name="password" class="input-block-level" placeholder="Password">
            <label class="checkbox">
                <input type="checkbox" value="remember-me"> Remember me
            </label>
            <button class="btn btn-large btn-primary" type="submit">Sign in</button>
        </form>
    </div>
</%block>
