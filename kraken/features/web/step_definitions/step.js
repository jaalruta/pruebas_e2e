const { Given, When, Then } = require('@cucumber/cucumber');

When('I enter email {string}', async function (email) {

    let element = await this.driver.$('#ember7');

    return await element.setValue(email);

});

When('I enter password {string}', async function (password) {

    let element = await this.driver.$('#ember9');

    return await element.setValue(password);

});

When('I click next', async function() {

    let element = await this.driver.$('#ember11');

    return await element.click();

})

When('I click posts', async function() {

    let element = await this.driver.$('#ember46');

    return await element.click();

})

When('I click new posts', async function() {

    let element = await this.driver.$(".gh-main a[href='#/editor/post/']");
    return await element.click();

})


When('I enter post title {string}', async function (titulo) {

    let element = await this.driver.$('.gh-editor-title');

    return await element.setValue(titulo);

});


When('I enter post body {string}', async function (body) {

    let element = await this.driver.$('.koenig-editor__editor');
    return await element.setValue(body);
});

When('I click publish menu', async function() {

    let element = await this.driver.$('.gh-publishmenu div');

    return await element.click();

})


When('I click publish', async function() {

    let element = await this.driver.$('.gh-publishmenu-button');

    return await element.click();

})

When('I click publish confirm', async function() {

    let element = await this.driver.$('.modal-footer button:nth-child(2)');
    return await element.click();

})



When('I click Schedule it for later', async function() {

    let element = await this.driver.$('.gh-date-time-picker');
    return await element.click();

})


When('I click members', async function() {

    let element = await this.driver.$(".gh-nav-body a[href='#/members/']");

    return await element.click();

})


When('I click new member', async function() {

    let element = await this.driver.$(".gh-canvas-header a[href='#/members/new/']");
    return await element.click();

})


When('I enter member name {string}', async function (name) {

    let element = await this.driver.$('#member-name');

    return await element.setValue(name);

});


When('I enter member email {string}', async function (email) {

    let element = await this.driver.$('#member-email');

    return await element.setValue(email);

});

When('I enter member note {string}', async function (note) {

    let element = await this.driver.$('#member-note');

    return await element.setValue(note);

});


When('I click save', async function() {

    let element = await this.driver.$(".view-actions button.gh-btn-primary");
    return await element.click();

})

When('I select a member', async function() {

    let element = await this.driver.$(".gh-main tr:nth-child(2) a:nth-child(1)");
    return await element.click();

})

When('I click config member', async function() {

    let element = await this.driver.$(".view-actions .dropdown button.gh-btn-icon");
    return await element.click();

})

When('I click delete member', async function() {

    let element = await this.driver.$(".gh-member-actions-menu li:nth-child(2) button");
    return await element.click();

})

When('I click confirm delete', async function() {

    let element = await this.driver.$(".modal-footer .gh-btn-red");
    return await element.click();

})
