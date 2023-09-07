import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import axios from 'axios';
import { ChatbotService } from '../../../app/chatbot.service'

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent {
  userInput: string = '';
  botResponse: string = '';
  showChatbox = false;
  constructor(private chatbotService: ChatbotService) { }

  async sendUserInput() {
    if (this.userInput.trim() === '') {
      return;
    }

    const userMessage = this.userInput;
    this.userInput = '';

    try {
      const response = await this.chatbotService.getBotResponse(userMessage);
      this.botResponse = response;

      // Add the user's message and bot's response to chat history

    } catch (error) {
      console.error('Error:', error);
      this.botResponse = 'An error occurred while processing your request.';
    }
  }


  toggleChatBox() {
    this.showChatbox = !this.showChatbox;
    
  }
}
