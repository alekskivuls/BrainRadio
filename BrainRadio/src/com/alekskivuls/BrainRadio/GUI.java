package com.alekskivuls.BrainRadio;

import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.KeyEvent;

import javax.swing.AbstractButton;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

class GUI extends JFrame
{
  JPanel panel;
  JLabel label;
  JButton b1,b2,b3,b4,b5,b6,b7,b8,b9,b10;

  // constructor
  public GUI( String title )
  {
    super( title );                      // invoke the JFrame constructor
    setSize( 500, 500);
    setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
    
    setLayout( new GridLayout(0,2) );       // set the layout manager
    
    b1 = new JButton("Player 1 Status");
    b1.setVerticalTextPosition(AbstractButton.CENTER);
    b1.setHorizontalTextPosition(AbstractButton.LEADING);
    b1.setMnemonic(KeyEvent.VK_D);
    b1.setActionCommand("disable");
    add(b1);
    b1.setBackground(Color.GREEN);
    b2 = new JButton("Player 2 Status");
    add(b2);
    b2.setBackground(Color.GREEN);
    b3 = new JButton("Player 3 Status");
    add(b3);
    b3.setBackground(Color.GREEN);
    b4 = new JButton("Player 4 Status");
    add(b4);
    b4.setBackground(Color.GREEN);
    b5 = new JButton("Player 5 Status");
    b5.setBackground(Color.RED);
    add(b5);
    b6 = new JButton("Player 6 Status");
    add(b6);
    b6.setBackground(Color.GREEN);
    b7 = new JButton("Player 7 Status");
    add(b7);
    b7.setBackground(Color.GREEN);
    b8 = new JButton("Player 8 Status");
    add(b8);
    b8.setBackground(Color.GREEN);
    b9 = new JButton("Player 9 Status");
    add(b9);
    b9.setBackground(Color.GREEN);
    b10 = new JButton("Player 10 Status");
    add(b10);
    b10.setBackground(Color.GREEN);
  }
 
} 