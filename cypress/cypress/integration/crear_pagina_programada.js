describe ('crear pagina programada', function(){
  beforeEach(() => {
      cy.visit('http://localhost:2368/ghost')
      cy.wait(5000)
    })
  it ('login', function(){
      cy.visit("http://localhost:2368/ghost/#/signin");
      cy.get('#ember7').type(Cypress.config('usuario'));
      cy.get('#ember9').type(Cypress.config('pass'));
      cy.get('#ember11').click();
      cy.wait(2000);
      cy.get('#ember28').click();
      cy.wait(3000);
      cy.get('.ember-view.gh-btn.gh-btn-primary.view-actions-top-row').click();
      cy.get('.gh-editor-title.ember-text-area.gh-input.ember-view').type("Pagina de prueba");
      cy.wait(2000);
      cy.get('.koenig-editor__editor.__mobiledoc-editor').type("Descripcion pagina");
      cy.get('.ember-view.ember-basic-dropdown-trigger.gh-btn.gh-btn-editor.gh-publishmenu-trigger').click();
      cy.wait(1000);
      cy.get('.gh-date-time-picker').click();
      cy.get('.gh-publishmenu-button').click();
      cy.get('.gh-btn.gh-btn-black.gh-btn-icon.ember-view').click();
      cy.get('.ember-view.gh-editor-back-button').click();
      
  })
})

