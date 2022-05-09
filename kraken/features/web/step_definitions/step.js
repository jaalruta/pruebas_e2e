const { Given, When, Then } = require('@cucumber/cucumber');
const expect = require('chai').expect;
When('I enter email {kraken-string}', async function (email) {

    let element = await this.driver.$('#ember7');

    return await element.setValue(email);

});

When('I enter password {kraken-string}', async function (password) {

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

When('I click setting', async function() {

    let element = await this.driver.$(".gh-nav-body a[href='#/settings/']");
    return await element.click();

})


When('I click general', async function() {

    let element = await this.driver.$(".view-container a[href='#/settings/general/']");
    return await element.click();

})

When('I expand lenguage option', async function() {

    let element = await this.driver.$("body > div:nth-child(4) > div:nth-child(3) > main:nth-child(2) > section:nth-child(1) > div:nth-child(2) > section:nth-child(2) > div:nth-child(3) > div:nth-child(1) > button:nth-child(2) > span:nth-child(1)");
    return await element.click();

})


When('I enter lenguage {string}', async function (lenguage) {

    let element = await this.driver.$('.ember-text-field.gh-input.ember-view');

    return await element.setValue(lenguage);

});


When('I click staff', async function() {

    let element = await this.driver.$(".view-container a[href='#/settings/staff/']");
    return await element.click();

})


When('I click invite people', async function() {

    let element = await this.driver.$(".view-actions button.gh-btn-primary");
    return await element.click();

})

When('I enter invite email {string}', async function (email) {

    let element = await this.driver.$('#new-user-email');

    return await element.setValue(email);

});



When('I click send invitation', async function() {

    let element = await this.driver.$(".modal-footer button");
    return await element.click();

})

When('I click revoke staff', async function() {

    let element = await this.driver.$("div[class='apps-grid'] div:nth-child(1) article:nth-child(1) div:nth-child(2) div:nth-child(1) a:nth-child(1)");
    return await element.click();
})


When('I click close invite', async function() {

    let element = await this.driver.$("a[title='Close']");
    return await element.click();
})

When('I click over a staff member', async function() {

    let element = await this.driver.$(".apps-grid-cell.tooltip-centered a");
    return await element.click();
})

When('I enter staff name {string}', async function (name) {

    let element = await this.driver.$('#user-name');

    return await element.setValue(name);

});

When('I enter staff bio {string}', async function (bio) {

    let element = await this.driver.$('#user-bio');

    return await element.setValue(bio);

});

When('I click tags', async function() {

    let element = await this.driver.$(".gh-nav-list a[href='#/tags/']"); 

    return await element.click();

})

When('I click new tag', async function() {

    let element = await this.driver.$(".gh-canvas-header a[href='#/tags/new/']"); 
    return await element.click();

})

When('I enter tag name {string}', async function (name) {

    let element = await this.driver.$('#tag-name'); 

    return await element.setValue(name);

});

When('I enter tag description {string}', async function (description) {

    let element = await this.driver.$('#tag-description'); 

    return await element.setValue(description);

});

When('I select a tag edicion', async function() {

    let element = await this.driver.$(".gh-canvas a[href='#/tags/segundo-tag/']"); 
    return await element.click();

});

When('I select a tag borrado', async function() {

    let element = await this.driver.$(".gh-canvas a[href='#/tags/prueba-borrado/']"); 
    return await element.click();

});

When('I click delete tag', async function() {

    let element = await this.driver.$(".gh-btn-red"); 
    return await element.click();

});


Then('the lenguage must be {string}', async function (lenguage) {
    let element = await this.driver.$('.ember-text-field.gh-input.ember-view');
    let valor = await element.getValue()
    expect(valor).to.equal(lenguage);
  });


Then('the member must be created', async function () {
    let element = await this.driver.$$('.gh-member-details-meta');
    let valor = element.length >0 
    expect(valor).to.equal(true);
  });

Then('the member name must be {string}', async function (name) {
    let element = await this.driver.$('#member-name');
    let valor = await element.getValue()
    expect(valor).to.equal(name);
  });

Then('the member {string} must be delete', async function (name) {
    let busqueda = "="+name;
    let element = await this.driver.$$(busqueda);
    let valor = element.length >0 
    expect(valor).to.equal(false);
});

Then('the tag must be created', async function () {
    let element = await this.driver.$$(".tags-list a[href='#/tags/primer-tag/']");
    let valor = element.length >0
    expect(valor).to.equal(true);
  });

Then('the tag name must be {string}', async function (name) {
    let element = await this.driver.$('#tag-name');
    let valor = await element.getValue()
    expect(valor).to.equal(name);
  });

  Then('the tag {string} must be delete', async function (name) {
    let busqueda = "="+name;
    let element = await this.driver.$$(busqueda);
    let valor = element.length >0 
    expect(valor).to.equal(false);
});

When('I click post menu', async function() {

    let element = await this.driver.$('.ember-view.gh-editor-back-button');
    return await element.click();

})

When('I click posts edit', async function() {

    let element = await this.driver.$('.posts-list > :nth-child(2)');
    return await element.click();

})

When('I click post publish', async function() {

    let element = await this.driver.$('.ember-view.gh-secondary-action.gh-nav-new-post');
    return await element.click();

})

When('I click post settings', async function() {

    let element = await this.driver.$('.settings-menu-toggle > span > svg');
    return await element.click();

})

When('I click delete post', async function() {

    let element = await this.driver.$('form > .gh-btn > span');
    return await element.click();

})

When('I click confirm delete post', async function() {

    let element = await this.driver.$('.gh-btn.gh-btn-red.gh-btn-icon.ember-view');
    return await element.click();

})


When('I click pages', async function() {

  let element = await this.driver.$('#ember28');

  return await element.click();

})

When('I click new pages', async function() {

  let element = await this.driver.$(".ember-view.gh-btn.gh-btn-primary.view-actions-top-row");
  return await element.click();

})


When('I enter pages title {string}', async function (titulo) {

  let element = await this.driver.$('.gh-editor-title.ember-text-area.gh-input.ember-view');

  return await element.setValue(titulo);

});


When('I enter pages body {string}', async function (body) {

  let element = await this.driver.$('.koenig-editor__editor.__mobiledoc-editor');
  return await element.setValue(body);
});


When('I click pages menu', async function() {

  let element = await this.driver.$('.ember-view.gh-editor-back-button');
  return await element.click();

})

When('I click pages edit', async function() {

  let element = await this.driver.$('.gh-content-entry-title');
  return await element.click();
})

When('I click page settings', async function() {

  let element = await this.driver.$('.settings-menu-toggle > span > svg');
  return await element.click();

})

When('I click delete page', async function() {

  let element = await this.driver.$('form > .gh-btn > span');
  return await element.click();

})

When('I click confirm delete page', async function() {

  let element = await this.driver.$('.gh-btn.gh-btn-red.gh-btn-icon.ember-view');
  return await element.click();

})

When('I expand zone option', async function() {

      let element = await this.driver.$(':nth-child(2) > .gh-expandable > :nth-child(2) > .gh-expandable-header > .gh-btn > span');
      return await element.click();

})

When('I choose zone option', async function() {

  let element = await this.driver.$("select");
  return await element.select(Pacific/Pago_Pago);

}) 