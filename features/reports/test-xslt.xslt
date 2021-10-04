 <xsl:stylesheet version="1.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:template match="/">
         <div class="toc-contents">
             <ul>
                 <xsl:apply-templates/>
             </ul>
         </div>
     </xsl:template>
     <xsl:template match="part">
         <li>
          <div class="toc-part">
              <h1><xsl:value-of select="@title"/></h1>
              <ul>
                  <xsl:apply-templates select="chapter"/>
              </ul>
          </div>
         </li>
     </xsl:template>
     <xsl:template match="chapter">
         <li>
          <div class="toc-chapter">
              <h2><xsl:value-of select="@title"/></h2>
              <ul>
                  <xsl:apply-templates select=".//leaf"/>
              </ul>
          </div>             
         </li>
     </xsl:template>
     <xsl:template match="leaf">
 
         <li>
             <a>
                 <xsl:attribute name="href">
                     http://makble.com/<xsl:value-of select="@seotitle"/>
                </xsl:attribute>
              <xsl:value-of select="@title"/></a>
         </li>
     </xsl:template>
 </xsl:stylesheet>
