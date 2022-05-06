describe ('cambiar lenguaje', function(){
    beforeEach(() => {
        cy.visit('http://localhost:2368/ghost')
        cy.wait(5000)
      })

    it ('cambiar lenguaje', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type(Cypress.config('usuario'));
        cy.get('#ember9').type(Cypress.config('pass'));
        cy.get('#ember11').click();
        cy.wait(5000);
        cy.get(".gh-nav-body a[href='#/settings/']").click();
        cy.wait(2000);
        cy.get(".view-container a[href='#/settings/general/']").click();
        cy.wait(2000);
        cy.get("body > div:nth-child(4) > div:nth-child(3) > main:nth-child(2) > section:nth-child(1) > div:nth-child(2) > section:nth-child(2) > div:nth-child(3) > div:nth-child(1) > button:nth-child(2) > span:nth-child(1)").click();
        cy.wait(2000);
        cy.get('.ember-text-field.gh-input.ember-view').type('{selectall}{backspace}es');
        cy.get(".view-actions button.gh-btn-primary").click();
        cy.wait(2000);

        cy.get('.ember-text-field.gh-input.ember-view').should('have.value', 'es')
    })
})