describe ('borrar', function(){
    beforeEach(() => {
        cy.visit('http://localhost:2368/ghost')
        cy.wait(5000)
      })

    it ('login', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type(Cypress.config('usuario'));
        cy.get('#ember9').type(Cypress.config('pass'));
        cy.get('#ember11').click();
        cy.wait(1000);
        
        cy.get('.ember-view.gh-secondary-action.gh-nav-new-post').click();
        cy.wait(1000);
        cy.get('.gh-editor-title.ember-text-area.gh-input.ember-view').type('POST DE PRUEBA PARA BORRAR');
        cy.wait(2000);
        cy.get('.koenig-editor__editor').type("PRUEBAS AUTOMATIZADAS MISO");
        cy.get('.ember-view.ember-basic-dropdown-trigger.gh-btn.gh-btn-editor.gh-publishmenu-trigger').click();
        cy.get('.gh-btn.gh-btn-black.gh-publishmenu-button.gh-btn-icon.ember-view').click();
        cy.get('.gh-btn.gh-btn-black.gh-btn-icon.ember-view').click();
        cy.wait(1000);
        cy.get('.ember-view.gh-editor-back-button').click();
        cy.get('.posts-list > :nth-child(2)').click();
        cy.get('.settings-menu-toggle > span > svg').click();
        cy.get('form > .gh-btn > span').click();
        cy.get('.gh-btn.gh-btn-red.gh-btn-icon.ember-view').click();
    })
})